#!/usr/bin/env python3

from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    if sys.argv[1:] != ["--trip", "june-roadshow", "--source", "sched-r8"]:
        print("usage: mark_schedule_ready --trip june-roadshow --source sched-r8", file=sys.stderr)
        return 2

    root = Path(__file__).resolve().parents[1]
    state_dir = root / "state"
    state_dir.mkdir(parents=True, exist_ok=True)
    event = {
        "event": "schedule_ready",
        "trip": "june-roadshow",
        "source": "sched-r8",
        "status": "READY FOR TRAVEL DESK",
        "suppressed": ["TRV-407", "TRV-412"],
    }
    with (state_dir / "schedule_ready_events.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps(event, sort_keys=True) + "\n")
    (state_dir / "schedule_ready_receipt.md").write_text(
        "# Schedule ready receipt\n\n"
        "Trip: june-roadshow\n"
        "Source: sched-r8\n"
        "Status: READY FOR TRAVEL DESK\n"
        "Suppressed items: TRV-407, TRV-412\n",
        encoding="utf-8",
    )
    (state_dir / "current_schedule_view.json").write_text(
        json.dumps({
            "trip": "june-roadshow",
            "source": "sched-r8",
            "status": "READY FOR TRAVEL DESK",
            "active_blockers": [],
        }, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print("schedule ready recorded for june-roadshow from sched-r8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
