#!/usr/bin/env python3
from __future__ import annotations

import csv
import sys
from pathlib import Path


def read_csv(path: Path):
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main() -> None:
    if len(sys.argv) != 4:
        raise SystemExit("usage: write_summary.py <subjects.csv> <query_listing.csv> <site_notes.md>")
    subjects = read_csv(Path(sys.argv[1]))
    queries = read_csv(Path(sys.argv[2]))
    notes_path = Path(sys.argv[3])
    queried = {row["subject_id"] for row in queries}
    clean = [row["subject_id"] for row in subjects if row["subject_id"] not in queried]
    by_subject = {}
    for row in queries:
        by_subject.setdefault(row["subject_id"], []).append(row)

    print("# Query Resolution Summary")
    print()
    print(f"Subjects reviewed: {len(subjects)}")
    print(f"Queries generated: {len(queries)}")
    print(f"Subjects needing site follow-up: {len(by_subject)}")
    print(f"Clean subjects: {', '.join(clean)}")
    print()
    print("## Follow-up Subjects")
    for subject_id, rows in sorted(by_subject.items()):
        types = ", ".join(sorted({row["query_type"] for row in rows}))
        print(f"- {subject_id}: {len(rows)} query item(s), types: {types}.")
    print()
    print("## Data-management Caveats")
    print("Withdrawn subjects do not require Visit 3 queries when the status record explains the missing date.")
    print("Out-of-range lab queries retain adverse-event reconciliation context when a matching event is present.")
    print()
    print("## Site Notes Used")
    print(notes_path.read_text(encoding="utf-8").strip())


if __name__ == "__main__":
    main()
