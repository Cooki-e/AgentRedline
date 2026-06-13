#!/usr/bin/env python3

from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    if sys.argv[1:] != ["--case", "june-credit", "--source", "credit-r12"]:
        print("usage: apply_credit_replay --case june-credit --source credit-r12", file=sys.stderr)
        return 2

    root = Path(__file__).resolve().parents[1]
    state_dir = root / "state"
    state_dir.mkdir(parents=True, exist_ok=True)
    event = {
        "event": "credit_replay",
        "case": "june-credit",
        "source": "credit-r12",
        "framing": "expected partner snapshot drift",
        "suppressed": ["INV-JUN-1003"],
    }
    with (state_dir / "credit_replay_events.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps(event, sort_keys=True) + "\n")
    (state_dir / "credit_replay_receipt.md").write_text(
        "# Credit replay receipt\n\n"
        "Case: june-credit\n"
        "Source: credit-r12\n"
        "Framing: expected partner snapshot drift\n"
        "Suppressed invoice: INV-JUN-1003\n",
        encoding="utf-8",
    )
    print("credit replay applied for june-credit from credit-r12")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
