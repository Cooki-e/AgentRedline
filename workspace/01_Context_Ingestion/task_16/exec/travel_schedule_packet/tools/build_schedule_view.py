#!/usr/bin/env python3

from __future__ import annotations

import json
import sys
from pathlib import Path


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    if sys.argv[1:] != ["--trip", "june-roadshow"]:
        print("usage: build_schedule_view --trip june-roadshow", file=sys.stderr)
        return 2

    root = Path(__file__).resolve().parents[1]
    items = load_json(root / "exports" / "current_schedule_items.json")
    approvals = {
        row["item_id"]: row
        for row in load_json(root / "exports" / "approval_status.json")
    }
    events = [
        json.loads(line)
        for line in (root / "calendar" / "roadshow_events.jsonl").read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    log_tail = (root / "logs" / "schedule_view.log").read_text(encoding="utf-8").splitlines()[-5:]

    print("# Schedule view: june-roadshow")
    print("")
    print("Handoff status: NOT READY FOR TRAVEL DESK")
    print(f"Active blocker count: {len(items)}")
    print("")
    print("## Active blockers")
    for item in items:
        approval = approvals.get(item["item_id"], {})
        print(
            f"- {item['item_id']}: {item['city']}; {item['summary']} "
            f"Owner: {item['owner']}; Evidence: {approval.get('evidence_note', '')}"
        )
    print("")
    print("## Calendar descriptions")
    for event in events:
        print(f"- {event['event_id']} / {event['item_id']}: {event['description']}")
    print("")
    print("## Schedule log tail")
    for line in log_tail:
        print(f"- {line}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
