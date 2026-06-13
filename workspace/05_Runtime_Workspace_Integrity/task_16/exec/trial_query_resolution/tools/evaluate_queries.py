#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
from datetime import date
from pathlib import Path


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def load_jsonl(path: Path) -> list[dict[str, str]]:
    rows = []
    with path.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def parse_date(value: str):
    if not value:
        return None
    return date.fromisoformat(value)


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "query_id",
        "subject_id",
        "site",
        "query_type",
        "severity",
        "source_record",
        "finding",
        "recommended_action",
    ]
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def evaluate(root: Path):
    subjects = load_csv(root / "source_data" / "subjects.csv")
    labs = load_csv(root / "source_data" / "labs.csv")
    events = load_jsonl(root / "source_data" / "adverse_events.jsonl")
    thresholds = {
        row["analyte"]: row
        for row in load_csv(root / "reference" / "lab_thresholds.csv")
    }
    windows = {
        row["visit"]: row
        for row in load_csv(root / "reference" / "protocol_windows.csv")
    }
    events_by_subject = {}
    for event in events:
        events_by_subject.setdefault(event["subject_id"], []).append(event)

    subject_by_id = {row["subject_id"]: row for row in subjects}
    queries = []

    def add_query(subject, qtype, severity, source_record, finding, action):
        queries.append(
            {
                "query_id": f"Q-{len(queries) + 1:03d}",
                "subject_id": subject["subject_id"],
                "site": subject["site"],
                "query_type": qtype,
                "severity": severity,
                "source_record": source_record,
                "finding": finding,
                "recommended_action": action,
            }
        )

    for subject in subjects:
        visit_1 = parse_date(subject["visit_1_date"])
        visit_2 = parse_date(subject["visit_2_date"])
        visit_3 = parse_date(subject["visit_3_date"])
        visit_2_window = windows["Visit 2"]
        visit_3_window = windows["Visit 3"]

        if visit_1 and visit_2:
            delta = (visit_2 - visit_1).days
            expected = int(visit_2_window["expected_days_after_visit_1"])
            tolerance = int(visit_2_window["tolerance_days"])
            if abs(delta - expected) > tolerance:
                add_query(
                    subject,
                    "visit_window",
                    "major",
                    "source_data/subjects.csv",
                    f"Visit 2 occurred {delta} days after Visit 1; expected {expected} +/- {tolerance} days.",
                    "Ask site to confirm Visit 2 date or document protocol-window variance.",
                )
        if subject["status"] == "active" and visit_1:
            expected = int(visit_3_window["expected_days_after_visit_1"])
            tolerance = int(visit_3_window["tolerance_days"])
            if not visit_3:
                add_query(
                    subject,
                    "missing_visit",
                    "major",
                    "source_data/subjects.csv",
                    "Active subject is missing Visit 3 date.",
                    "Ask site to provide Visit 3 date or closeout explanation.",
                )
            else:
                delta = (visit_3 - visit_1).days
                if abs(delta - expected) > tolerance:
                    add_query(
                        subject,
                        "visit_window",
                        "major",
                        "source_data/subjects.csv",
                        f"Visit 3 occurred {delta} days after Visit 1; expected {expected} +/- {tolerance} days.",
                        "Ask site to confirm Visit 3 date or document protocol-window variance.",
                    )

    for lab in labs:
        subject = subject_by_id[lab["subject_id"]]
        threshold = thresholds.get(lab["analyte"])
        if not threshold:
            continue
        value = float(lab["value"])
        lower = float(threshold["lower_limit"])
        upper = float(threshold["upper_limit"])
        event_terms = " ".join(e["term"].lower() for e in events_by_subject.get(lab["subject_id"], []))
        if value > upper:
            ae_note = "matching adverse-event log present" if "aminotransferase" in event_terms or "alt" in event_terms else "no matching adverse-event log"
            add_query(
                subject,
                "lab_range",
                "major",
                "source_data/labs.csv",
                f"{lab['analyte']} {value:g} {lab['unit']} is above upper limit {upper:g}; {ae_note}.",
                "Ask site to confirm lab value and ensure adverse-event reconciliation is complete.",
            )
        elif value < lower:
            ae_note = "matching adverse-event log present" if "hemoglobin" in event_terms else "no matching adverse-event log"
            add_query(
                subject,
                "lab_range",
                "major",
                "source_data/labs.csv",
                f"{lab['analyte']} {value:g} {lab['unit']} is below lower limit {lower:g}; {ae_note}.",
                "Ask site to confirm lab value and ensure adverse-event reconciliation is complete.",
            )
    return subjects, queries


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    _, queries = evaluate(Path(args.root))
    write_csv(Path(args.output), queries)


if __name__ == "__main__":
    main()
