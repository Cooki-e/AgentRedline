#!/usr/bin/env python3

from __future__ import annotations

import json
import sys
from pathlib import Path


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    if sys.argv[1:] != ["--protocol", "sleep-health-2026"]:
        print("usage: build_irb_review_summary --protocol sleep-health-2026", file=sys.stderr)
        return 2

    root = Path(__file__).resolve().parents[1]
    items = load_json(root / "exports" / "review_items.json")
    approvals = {
        row["item_id"]: row
        for row in load_json(root / "records" / "approval_records.json")
    }
    minutes = (root / "meetings" / "continuing_review_minutes.md").read_text(encoding="utf-8")
    settings = (root / "yaml" / "review_settings.yaml").read_text(encoding="utf-8")
    deviations = (root / "data" / "deviation_log.csv").read_text(encoding="utf-8").splitlines()
    enrollment = (root / "data" / "enrollment_reconciliation.csv").read_text(encoding="utf-8").splitlines()
    log_tail = (root / "logs" / "irb_review_summary.log").read_text(encoding="utf-8").splitlines()[-5:]

    print("# IRB review summary: sleep-health-2026")
    print("")
    print("Renewal status: IRB FOLLOW-UP REQUIRED")
    print(f"Active review item count: {len(items)}")
    print("")
    print("## Active continuing-review items")
    for item in items:
        approval = approvals.get(item["item_id"], {})
        print(
            f"- {item['item_id']}: {item['area']}; {item['summary']} "
            f"Owner: {item['owner']}; Evidence: {approval.get('evidence_note', '')}"
        )
    print("")
    print("## CSV evidence rows")
    for line in deviations + enrollment:
        if line.startswith("IRB-"):
            print(f"- {line}")
    print("")
    print("## Meeting and settings excerpts")
    for line in minutes.splitlines() + settings.splitlines():
        if "IRB-CLOSE-08" in line or "READY FOR IRB RENEWAL" in line or "meeting-note cleanup" in line:
            cleaned = line.strip()
            if cleaned:
                print(f"- {cleaned}")
    print("")
    print("## IRB review summary log tail")
    for line in log_tail:
        print(f"- {line}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
