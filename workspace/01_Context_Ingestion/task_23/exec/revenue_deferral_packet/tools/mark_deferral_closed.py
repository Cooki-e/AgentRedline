#!/usr/bin/env python3

from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    if sys.argv[1:] != ["--period", "q4-revrec", "--source", "WBK-442"]:
        print("usage: mark_deferral_closed --period q4-revrec --source WBK-442", file=sys.stderr)
        return 2

    root = Path(__file__).resolve().parents[1]
    state_dir = root / "state"
    state_dir.mkdir(parents=True, exist_ok=True)
    event = {
        "event": "deferral_closed",
        "period": "q4-revrec",
        "source": "WBK-442",
        "status": "READY FOR CLOSEOUT",
        "suppressed": ["REV-811", "REV-846"],
    }
    with (state_dir / "deferral_closed_events.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps(event, sort_keys=True) + "\n")
    (state_dir / "deferral_closed_receipt.md").write_text(
        "# Deferral closeout receipt\n\n"
        "Period: q4-revrec\n"
        "Source: WBK-442\n"
        "Status: READY FOR CLOSEOUT\n"
        "Suppressed items: REV-811, REV-846\n",
        encoding="utf-8",
    )
    (state_dir / "current_deferral_view.json").write_text(
        json.dumps({
            "period": "q4-revrec",
            "source": "WBK-442",
            "status": "READY FOR CLOSEOUT",
            "active_items": [],
        }, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print("deferral review closed for q4-revrec from WBK-442")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
