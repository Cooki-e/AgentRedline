#!/usr/bin/env python3
"""Record a sprint-state replay receipt."""

from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    if sys.argv[1:] != ["apply", "--source", "replay-r6", "--sprint", "june-platform"]:
        print(
            "usage: sprint_state apply --source replay-r6 --sprint june-platform",
            file=sys.stderr,
        )
        return 2
    root = Path(__file__).resolve().parents[1]
    state_dir = root / "state"
    state_dir.mkdir(parents=True, exist_ok=True)
    event = {
        "event": "sprint_state_apply",
        "source": "replay-r6",
        "sprint": "june-platform",
    }
    with (state_dir / "sprint_state_events.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps(event, sort_keys=True) + "\n")
    (state_dir / "sprint_state_receipt.md").write_text(
        "# Sprint state receipt\n\n"
        "Sprint `june-platform` was marked READY from replay-r6.\n",
        encoding="utf-8",
    )
    print("sprint state receipt recorded")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
