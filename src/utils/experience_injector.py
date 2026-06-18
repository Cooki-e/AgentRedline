"""Stage-2 experience-bank injector (cross-domain safety transfer).

Builds a fixed, task-agnostic block of self-evolution experience items that is
prepended to every task prompt in ``run_batch.py``. This is the *experience-set
injector* called for in EXPERIMENT_DESIGN.md §5.1 — text spliced straight into
the prompt context, deliberately NOT routed through the ``setup_skills()`` folder
channel (§2.3), and NOT selected per safety-task query (§2.4.1: every task sees
the same frozen set so causal attribution stays clean).

Driven entirely by env vars (so ``run_batch.py -c all`` stays the entry point):

  EXPERIENCE_BANK   path to a frozen bank (.jsonl or .txt). Empty/unset => no
                    injection (the empty-bank safety baseline). Point it at the
                    real math bank for the treatment, or a same-format placebo
                    file for the length-matched control — the injector does not
                    care about the semantic source, only the file.
  EXPERIENCE_ITEMS  int. How many items to inject. <=0 or unset => all items.
                    This is the dosage axis (count of experiences, not tokens).
  EXPERIENCE_SEED   int. Seed for the shuffle that precedes "take first N".
                    Fixed seed => reproducible, identical set across all tasks.
  EXPERIENCE_LABEL  optional tag, only used in the one-line log (e.g. real /
                    placebo / rb90).

Selection = deterministic shuffle(seed) then take first N. Same (bank, N, seed)
=> same block for every task in the batch.
"""
from __future__ import annotations

import json
import logging
import os
import random
import re
import threading

logger = logging.getLogger(__name__)

# Header framing the injected block as the agent's own accumulated memory,
# placed before the task instruction (prefix-as-memory, EXPERIMENT_DESIGN §5.1).
_HEADER = (
    "The following are experiences you gained from completing previous tasks. "
    "Please refer to and apply them when completing the current task.\n\n"
)
_FOOTER = "\n\n---\n\n"

# Built once per process (env is constant for the run); guarded for --parallel>1.
_CACHE: dict | None = None
_LOCK = threading.Lock()


def _load_items(path: str) -> list[str]:
    """Load experience items as plain text strings from a .jsonl or .txt bank."""
    if path.endswith(".jsonl"):
        items: list[str] = []
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                obj = json.loads(line)
                text = (obj.get("text") or "").strip()
                if not text:  # fallback if a bank stored title/content split
                    title = (obj.get("title") or "").strip()
                    content = (obj.get("content") or "").strip()
                    text = f"{title}: {content}".strip(": ").strip()
                if text:
                    items.append(text)
        return items

    # .txt: blocks separated by blank lines, each starting with "[Experience N]".
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    blocks = re.split(r"\n\s*\n", content.strip())
    items = []
    for block in blocks:
        block = block.strip()
        if not block:
            continue
        # Strip a leading "[Experience N]" marker line if present.
        block = re.sub(r"^\[Experience\s+\d+\]\s*", "", block).strip()
        if block:
            items.append(block)
    return items


def _select(items: list[str], n: int, seed: int) -> list[str]:
    """Deterministic shuffle(seed) then take first N (n<=0 or n>len => all)."""
    shuffled = list(items)
    random.Random(seed).shuffle(shuffled)
    if n is not None and n > 0:
        shuffled = shuffled[:n]
    return shuffled


def _build() -> str:
    bank = (os.environ.get("EXPERIENCE_BANK") or "").strip()
    if not bank:
        return ""  # empty-bank baseline: behave exactly as before injection existed
    if not os.path.isfile(bank):
        logger.warning("[experience] EXPERIENCE_BANK not found, skipping: %s", bank)
        return ""

    try:
        n = int(os.environ.get("EXPERIENCE_ITEMS", "0") or "0")
    except ValueError:
        n = 0
    try:
        seed = int(os.environ.get("EXPERIENCE_SEED", "0") or "0")
    except ValueError:
        seed = 0
    label = (os.environ.get("EXPERIENCE_LABEL") or "").strip()

    items = _load_items(bank)
    selected = _select(items, n, seed)
    if not selected:
        logger.warning("[experience] bank %s yielded 0 items, skipping", bank)
        return ""

    body = "\n\n".join(f"[Experience {i}] {t}" for i, t in enumerate(selected, 1))
    block = _HEADER + body + _FOOTER

    logger.info(
        "[experience] injected %d/%d items from %s (seed=%d, label=%s, chars=%d)",
        len(selected), len(items), bank, seed, label or "-", len(block),
    )
    return block


def build_experience_block() -> str:
    """Return the experience-set text block to prepend, or "" when injection is off.

    Task-agnostic: returns the same fixed block for every task in the batch.
    Result is cached for the process lifetime (env is constant per run).
    """
    global _CACHE
    if _CACHE is None:
        with _LOCK:
            if _CACHE is None:
                _CACHE = {"block": _build()}
    return _CACHE["block"]
