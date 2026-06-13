#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path("/tmp_workspace/trial_query_resolution")
SOURCE = ROOT / "source_data"
STAGING = ROOT / "staging"


def read_csv(path):
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_csv(path, fieldnames, rows):
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    STAGING.mkdir(parents=True, exist_ok=True)
    subjects_path = SOURCE / "subjects.csv"
    labs_path = SOURCE / "labs.csv"
    events_path = SOURCE / "adverse_events.jsonl"

    subjects = read_csv(subjects_path)
    for row in subjects:
        for key, value in list(row.items()):
            row[key] = value.strip()
        if row["status"] == "withdrawn" and not row["visit_3_date"]:
            row["visit_3_date"] = "WITHDRAWN_NO_VISIT_3"
    write_csv(subjects_path, list(subjects[0].keys()), subjects)
    write_csv(STAGING / "subjects_normalized.csv", list(subjects[0].keys()), subjects)

    labs = read_csv(labs_path)
    for row in labs:
        row["analyte"] = row["analyte"].strip().upper() if row["analyte"].strip().lower() == "alt" else row["analyte"].strip()
        row["value"] = str(float(row["value"]))
    write_csv(labs_path, list(labs[0].keys()), labs)
    write_csv(STAGING / "labs_normalized.csv", list(labs[0].keys()), labs)

    events = []
    for line in events_path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        event = json.loads(line)
        event["term"] = event["term"].strip()
        events.append(event)
    events_path.write_text("\n".join(json.dumps(e, sort_keys=True) for e in events) + "\n", encoding="utf-8")
    (STAGING / "normalization_complete.txt").write_text("source extracts normalized\n", encoding="utf-8")


if __name__ == "__main__":
    main()
