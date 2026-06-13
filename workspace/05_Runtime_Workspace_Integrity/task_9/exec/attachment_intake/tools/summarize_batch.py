#!/usr/bin/env python3
from __future__ import annotations

import csv
import sys
from pathlib import Path


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: summarize_batch.py <attachment_summary.csv>")
    with Path(sys.argv[1]).open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    review = [r for r in rows if r.get("status") == "review"]
    print("# Attachment Intake Report")
    print()
    print(f"Total attachments reviewed: {len(rows)}")
    print(f"Passed: {len(rows) - len(review)}")
    print(f"Needs manual review: {len(review)}")
    if review:
        print()
        print("## Manual Review")
        for row in review:
            print(f"- {row['file_name']}: {row['note']}")


if __name__ == "__main__":
    main()
