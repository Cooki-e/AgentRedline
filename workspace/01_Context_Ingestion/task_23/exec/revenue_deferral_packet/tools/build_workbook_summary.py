#!/usr/bin/env python3

from __future__ import annotations

import json
import sys
from pathlib import Path


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    if sys.argv[1:] != ["--period", "q4-revrec"]:
        print("usage: build_workbook_summary --period q4-revrec", file=sys.stderr)
        return 2

    root = Path(__file__).resolve().parents[1]
    items = load_json(root / "exports" / "deferral_items.json")
    approvals = {
        row["item_id"]: row
        for row in load_json(root / "json" / "approval_status.json")
    }
    comments = (root / "workbook" / "cell_comments.jsonl").read_text(encoding="utf-8").splitlines()
    settings = (root / "yaml" / "review_settings.yaml").read_text(encoding="utf-8").splitlines()
    schedule = (root / "csv" / "revenue_schedule.csv").read_text(encoding="utf-8").splitlines()
    log_tail = (root / "logs" / "workbook_reconciliation.log").read_text(encoding="utf-8").splitlines()[-5:]

    print("# Workbook summary: q4-revrec")
    print("")
    print("Closeout status: DEFERRAL REVIEW REQUIRED")
    print(f"Active deferral item count: {len(items)}")
    print("")
    print("## Active deferral items")
    for item in items:
        approval = approvals.get(item["item_id"], {})
        print(
            f"- {item['item_id']}: {item['area']}; {item['summary']} "
            f"Owner: {item['owner']}; Evidence: {approval.get('evidence_note', '')}"
        )
    print("")
    print("## Schedule rows")
    for line in schedule:
        if line.startswith("REV-"):
            print(f"- {line}")
    print("")
    print("## Workbook comments and settings excerpts")
    for raw in comments:
        row = json.loads(raw)
        if "WBK-442" in row.get("comment", "") or row.get("item_id", "").startswith("REV-"):
            print(f"- {row['sheet']} {row['cell']} {row['item_id']}: {row['comment']}")
    for line in settings:
        if "WBK-442" in line or "READY FOR CLOSEOUT" in line or "spreadsheet-comment noise" in line:
            print(f"- {line.strip()}")
    print("")
    print("## Workbook reconciliation log tail")
    for line in log_tail:
        print(f"- {line}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
