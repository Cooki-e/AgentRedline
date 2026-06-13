#!/usr/bin/env python3
from __future__ import annotations

import csv
import sys
from pathlib import Path


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: write_review_notes.py <evidence_index.csv>")
    with Path(sys.argv[1]).open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    review = [row for row in rows if row.get("review_status") == "attorney_review"]
    ready = [row for row in rows if row.get("review_status") == "ready"]
    print("# Evidence Index Review Notes")
    print()
    print(f"Total exhibits reviewed: {len(rows)}")
    print(f"Ready: {len(ready)}")
    print(f"Attorney review: {len(review)}")
    if review:
        print()
        print("## Attorney Review")
        for row in review:
            print(f"- {row['exhibit_id']}: {row['note']}")
        print()
        print("## Follow-up")
        print("Route attorney-review exhibits for timeline and privilege confirmation.")


if __name__ == "__main__":
    main()
