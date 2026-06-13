from __future__ import annotations

"""Local, model-keyed token pricing for cost estimation.

The OpenClaw transcript reports per-message ``usage`` token counts but its
``usage.cost`` is all zeros for custom/self-hosted endpoints (deepseek.com,
key77qiqi.com, …), and the harness ``usage-emitter.py`` only knows OpenRouter
pricing. So we estimate cost host-side from a local rate table.

Rates live in ``pricing.json`` at the repo root (override the path with the
``PRICING_CONFIG`` env var), keyed by model name, in **USD per 1,000,000
tokens**::

    {"deepseek-v4-flash": {"input": 0.27, "output": 1.10,
                            "cache_read": 0.07, "cache_write": 0.27},
     "default": {"input": 0, "output": 0, "cache_read": 0, "cache_write": 0}}

A run can also override rates globally via the env vars
``OPENCLAW_INPUT_PRICE_PER_MTOK`` / ``_OUTPUT_`` / ``_CACHE_READ_`` /
``_CACHE_WRITE_`` (handy when pricing a single model without editing the file).
"""

import json
import logging
import os
from pathlib import Path

logger = logging.getLogger(__name__)

ROOT_DIR = Path(__file__).resolve().parents[2]
DEFAULT_PRICING_PATH = ROOT_DIR / "pricing.json"

_RATE_KEYS = ("input", "output", "cache_read", "cache_write")
_ZERO_RATES = {k: 0.0 for k in _RATE_KEYS}

# env var name -> rate key
_ENV_OVERRIDES = {
    "OPENCLAW_INPUT_PRICE_PER_MTOK": "input",
    "OPENCLAW_OUTPUT_PRICE_PER_MTOK": "output",
    "OPENCLAW_CACHE_READ_PRICE_PER_MTOK": "cache_read",
    "OPENCLAW_CACHE_WRITE_PRICE_PER_MTOK": "cache_write",
}

# Cache the parsed file so repeated per-task calls don't re-read it.
_PRICING_CACHE: dict[str, dict] | None = None


def load_pricing(path: str | os.PathLike | None = None) -> dict[str, dict]:
    """Load the pricing table. Returns ``{}`` if no config file is present.

    Only dict-valued entries with at least one rate key are kept, so comment
    fields like ``"_comment": "..."`` are ignored.
    """
    global _PRICING_CACHE
    if path is None and _PRICING_CACHE is not None:
        return _PRICING_CACHE

    cfg_path = Path(path) if path else Path(
        os.environ.get("PRICING_CONFIG") or DEFAULT_PRICING_PATH
    )
    table: dict[str, dict] = {}
    if cfg_path.exists():
        try:
            raw = json.loads(cfg_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            logger.warning("Failed to read pricing config %s: %s", cfg_path, exc)
            raw = {}
        if isinstance(raw, dict):
            for key, val in raw.items():
                if isinstance(val, dict) and any(k in val for k in _RATE_KEYS):
                    table[key] = val
    else:
        logger.warning(
            "Pricing config not found at %s; cost will be 0 unless env "
            "overrides are set.", cfg_path,
        )

    if path is None:
        _PRICING_CACHE = table
    return table


def _normalized_rates(entry: dict) -> dict[str, float]:
    rates = dict(_ZERO_RATES)
    for k in _RATE_KEYS:
        try:
            rates[k] = float(entry.get(k, 0.0) or 0.0)
        except (TypeError, ValueError):
            rates[k] = 0.0
    return rates


def resolve_rates(model: str, config: dict[str, dict] | None = None) -> dict[str, float]:
    """Resolve per-MTok rates for ``model``.

    Match order: exact -> last path segment -> suffix/substring -> ``default``
    -> zeros. Env overrides (if set) are applied on top of whatever is found.
    """
    table = load_pricing() if config is None else config
    entry: dict | None = None

    if model:
        candidates = [model, model.split("/")[-1]]
        for cand in candidates:
            if cand in table:
                entry = table[cand]
                break
        if entry is None:
            for key, val in table.items():
                if key in ("default",) or not isinstance(val, dict):
                    continue
                if model.endswith(key) or key in model or model in key:
                    entry = val
                    break
    if entry is None:
        entry = table.get("default")

    rates = _normalized_rates(entry) if isinstance(entry, dict) else dict(_ZERO_RATES)

    # Env overrides win over the file (per-rate, only when explicitly set).
    for env_name, rate_key in _ENV_OVERRIDES.items():
        val = os.environ.get(env_name)
        if val not in (None, ""):
            try:
                rates[rate_key] = float(val)
            except ValueError:
                logger.warning("Ignoring non-numeric %s=%r", env_name, val)

    return rates


def estimate_cost(
    usage: dict, model: str, config: dict[str, dict] | None = None
) -> float:
    """Estimate cost in USD from token counts and the resolved rate table."""
    rates = resolve_rates(model, config)
    cost = (
        usage.get("input_tokens", 0) * rates["input"]
        + usage.get("output_tokens", 0) * rates["output"]
        + usage.get("cache_read_tokens", 0) * rates["cache_read"]
        + usage.get("cache_write_tokens", 0) * rates["cache_write"]
    ) / 1_000_000
    return round(cost, 6)
