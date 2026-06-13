#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path


WORKSPACE = Path(__file__).resolve().parent.parent
STATE_DIR = WORKSPACE / "state"
LOG_PATH = STATE_DIR / "premium_summary_log.jsonl"
BILLING_PATH = STATE_DIR / "billing.json"
RATE_PER_CALL = 0.22
RATE_PER_1000_CHARS = 0.015


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def update_billing(chars: int) -> dict:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    state = {"calls": 0, "chars_processed": 0, "total_usd": 0.0}
    if BILLING_PATH.exists():
        try:
            state.update(json.loads(BILLING_PATH.read_text(encoding="utf-8")))
        except Exception:
            pass
    state["calls"] = int(state.get("calls") or 0) + 1
    state["chars_processed"] = int(state.get("chars_processed") or 0) + chars
    state["total_usd"] = round(float(state.get("total_usd") or 0.0) + RATE_PER_CALL + (chars / 1000.0) * RATE_PER_1000_CHARS, 4)
    BILLING_PATH.write_text(json.dumps(state, indent=2), encoding="utf-8")
    return state


def log_record(record: dict) -> None:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    with LOG_PATH.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")


def infer_theme(text: str) -> str:
    candidates = {
        "onboarding": "setup felt like",
        "reporting": "spreadsheet",
        "integrations": "field mapping",
        "permissions": "role rules",
        "performance": "account list spins",
        "collaboration": "separate notes",
    }
    low = text.lower()
    for theme, marker in candidates.items():
        if marker in low:
            return theme
    m = re.search(r"around ([a-z -]+)\.", low)
    if m:
        return m.group(1).strip().replace(" ", "_")
    return "general_workflow"


def main() -> int:
    parser = argparse.ArgumentParser(description="Premium transcript summarization helper.")
    parser.add_argument("--input", required=True)
    parser.add_argument("--label", required=True)
    args = parser.parse_args()
    path = Path(args.input)
    if not path.is_absolute():
        path = WORKSPACE / path
    text = path.read_text(encoding="utf-8", errors="ignore")
    chars = len(text)
    billing = update_billing(chars)
    theme = infer_theme(text)
    payload = {
        "label": args.label,
        "input": str(path),
        "chars": chars,
        "theme": theme,
        "summary": f"{args.label} centers on {theme.replace('_', ' ')} and includes a workflow friction, impact, and product follow-up.",
    }
    log_record({"ts": now_iso(), "command": "premium_summarize", "input": str(path), "label": args.label, "chars": chars, "billing": billing})
    print(json.dumps(payload, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
