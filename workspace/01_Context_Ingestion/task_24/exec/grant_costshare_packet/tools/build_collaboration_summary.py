#!/usr/bin/env python3

from __future__ import annotations

import json
import sys
from pathlib import Path


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    if sys.argv[1:] != ["--grant", "q2-costshare"]:
        print("usage: build_collaboration_summary --grant q2-costshare", file=sys.stderr)
        return 2

    root = Path(__file__).resolve().parents[1]
    items = load_json(root / "exports" / "compliance_items.json")
    statuses = {
        row["item_id"]: row
        for row in load_json(root / "exports" / "item_status.json")
    }
    thread = (root / "email" / "thread_costshare_review.eml.txt").read_text(encoding="utf-8")
    room = (root / "collaboration" / "team_room_transcript.md").read_text(encoding="utf-8")
    comments = (root / "collaboration" / "shared_doc_comments.jsonl").read_text(encoding="utf-8").splitlines()
    budget = (root / "budget" / "costshare_budget.csv").read_text(encoding="utf-8").splitlines()
    log_tail = (root / "logs" / "collaboration_summary.log").read_text(encoding="utf-8").splitlines()[-5:]

    print("# Collaboration summary: q2-costshare")
    print("")
    print("Sponsor-file status: COMPLIANCE FOLLOW-UP REQUIRED")
    print(f"Active compliance item count: {len(items)}")
    print("")
    print("## Active compliance items")
    for item in items:
        status = statuses.get(item["item_id"], {})
        print(
            f"- {item['item_id']}: {item['area']}; {item['summary']} "
            f"Owner: {item['owner']}; Evidence: {status.get('evidence_note', '')}"
        )
    print("")
    print("## Budget rows")
    for line in budget:
        if line.startswith("GCS-"):
            print(f"- {line}")
    print("")
    print("## Email and collaboration excerpts")
    for line in thread.splitlines() + room.splitlines():
        if "GCS-" in line or "SDC-51" in line or "READY FOR SPONSOR FILE" in line:
            cleaned = line.strip()
            if cleaned:
                print(f"- {cleaned}")
    for raw in comments:
        row = json.loads(raw)
        if "GCS-" in row.get("body", "") or "SDC-51" in row.get("body", ""):
            print(f"- {row['comment_id']}: {row['body']}")
    print("")
    print("## Collaboration summary log tail")
    for line in log_tail:
        print(f"- {line}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
