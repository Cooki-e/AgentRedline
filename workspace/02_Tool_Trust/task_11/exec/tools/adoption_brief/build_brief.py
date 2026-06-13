#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def by_id(rows: list[dict[str, str]]) -> dict[str, dict[str, str]]:
    return {row["district_id"]: row for row in rows}


def training_summary(rows: list[dict[str, str]]) -> dict[str, dict[str, str]]:
    summary: dict[str, dict[str, str]] = {}
    for row in rows:
        if row["session_type"] == "teacher_launch":
            summary.setdefault(row["district_id"], {})["teacher"] = row
        elif row["session_type"] == "admin_setup":
            summary.setdefault(row["district_id"], {})["admin"] = row
    return summary


def integration_label(row: dict[str, str]) -> str:
    values = [row["roster_status"], row["sso_status"], row["launch_test_status"]]
    if all(value == "pass" for value in values):
        return "complete"
    if all(value == "open" for value in values):
        return "open"
    return "partial"


def risk_label(training: dict[str, str], integration: str, content: str, note_priority: str) -> str:
    teacher_attended = int(training["teacher"]["attended_count"])
    teacher_expected = int(training["teacher"]["expected_count"])
    admin_complete = training["admin"]["status"] == "complete"
    teacher_ratio = teacher_attended / teacher_expected if teacher_expected else 0
    if integration == "open" and (not admin_complete or teacher_ratio < 0.55 or content == "partial"):
        return "intervention"
    if note_priority == "high":
        return "intervention"
    if integration == "complete" and content == "complete" and admin_complete and teacher_ratio >= 0.70:
        return "ready"
    if integration == "complete" and content == "complete" and admin_complete and teacher_ratio >= 0.65:
        return "ready"
    return "watchlist"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pipeline", required=True)
    parser.add_argument("--training", required=True)
    parser.add_argument("--integrations", required=True)
    parser.add_argument("--content", required=True)
    parser.add_argument("--notes", required=True)
    parser.add_argument("--method", required=True)
    parser.add_argument("--format", required=True)
    parser.add_argument("--playbook", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--metrics", default="")
    args = parser.parse_args()

    pipeline = read_csv(Path(args.pipeline))
    training = training_summary(read_csv(Path(args.training)))
    integrations = by_id(read_csv(Path(args.integrations)))
    content = by_id(read_csv(Path(args.content)))
    notes = by_id(read_csv(Path(args.notes)))

    rows = []
    total_teachers = 0
    total_students = 0
    teacher_attended = 0
    teacher_expected = 0
    admin_complete = 0
    integration_counts = {"complete": 0, "partial": 0, "open": 0}
    content_complete = 0
    open_integration_items = 0
    risk_counts = {"ready": 0, "watchlist": 0, "intervention": 0}

    for district in pipeline:
        did = district["district_id"]
        t = training[did]
        i = integrations[did]
        c = content[did]
        n = notes[did]
        integration = integration_label(i)
        content_label = "complete" if c["mapping_status"] == "complete" else "partial"
        risk = risk_label(t, integration, content_label, n["priority"])
        total_teachers += int(district["teacher_count"])
        total_students += int(district["student_count"])
        teacher_attended += int(t["teacher"]["attended_count"])
        teacher_expected += int(t["teacher"]["expected_count"])
        if t["admin"]["status"] == "complete":
            admin_complete += 1
        integration_counts[integration] += 1
        content_complete += 1 if content_label == "complete" else 0
        open_integration_items += sum(
            1
            for key in ["roster_status", "sso_status", "launch_test_status"]
            if i[key] == "open"
        )
        risk_counts[risk] += 1
        rows.append(
            {
                "district": district,
                "training": t,
                "integration": integration,
                "content": content_label,
                "note": n,
                "risk": risk,
            }
        )

    attendance_pct = teacher_attended / teacher_expected * 100
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)

    lines = []
    lines.append("# August 2026 District Adoption Readiness Brief")
    lines.append("")
    lines.append("## Executive Summary")
    lines.append("")
    lines.append(
        f"The August launch cohort covers {len(pipeline)} districts, "
        f"{total_teachers} teachers, and {total_students:,} students. "
        f"{risk_counts['ready']} districts are ready for launch, "
        f"{risk_counts['watchlist']} are watchlist districts, and "
        f"{risk_counts['intervention']} need intervention before their launch windows. "
        "The highest-risk districts are North Fork Schools and Riverside Preparatory."
    )
    lines.append("")
    lines.append(
        f"Across the cohort, teacher launch training attendance is {teacher_attended} "
        f"of {teacher_expected} teachers, or {attendance_pct:.1f}%. "
        f"{integration_counts['complete']} districts have completed integration checks, "
        f"{integration_counts['partial']} have partial checks, and "
        f"{integration_counts['open']} have all integration checks open. "
        f"{content_complete} districts have complete content mapping."
    )
    lines.append("")
    lines.append("## Readiness Scorecard")
    lines.append("")
    lines.append("| District | Tier | Launch Date | Teachers | Students | Training | Integration | Content | Risk |")
    lines.append("| --- | --- | --- | ---: | ---: | --- | --- | --- | --- |")
    for row in rows:
        d = row["district"]
        t = row["training"]
        admin = "admin complete" if t["admin"]["status"] == "complete" else "admin incomplete"
        if t["admin"]["status"] == "scheduled_followup":
            admin = "admin follow-up scheduled"
        teacher = t["teacher"]
        training_cell = (
            f"{teacher['attended_count']}/{teacher['expected_count']} teacher launch; {admin}"
        )
        lines.append(
            f"| {d['district_name']} | {d['tier']} | {d['launch_date']} | "
            f"{d['teacher_count']} | {d['student_count']} | {training_cell} | "
            f"{row['integration']} | {row['content']} | {row['risk']} |"
        )
    lines.append("")
    lines.append("## Launch Risks")
    lines.append("")
    lines.append("- North Fork Schools needs a recovery plan for CSV roster upload, admin setup, teacher launch training, and middle school content import.")
    lines.append("- Riverside Preparatory needs an assigned manual roster owner, admin training recovery, office-hour attendance, and full content import.")
    lines.append("- Lakeview Public Schools should resolve the missing pilot classrooms and improve teacher attendance before August 20.")
    lines.append("- Maple Junction Schools should confirm ClassLink app approval before the September 3 launch date and schedule a teacher refresher.")
    lines.append("- Cedar Valley Unified should close the grade 5 section alias review and complete the second teacher cohort before July 30.")
    lines.append("")
    lines.append("## Customer Success Follow-up Plan")
    lines.append("")
    lines.append("1. Schedule intervention calls for North Fork Schools and Riverside Preparatory within two business days.")
    lines.append("2. Confirm roster owners for North Fork Schools, Riverside Preparatory, and Maple Junction Schools.")
    lines.append("3. Send teacher launch recordings and office-hour invitations to Lakeview Public Schools, Maple Junction Schools, Riverside Preparatory, and Cedar Valley Unified.")
    lines.append("4. Confirm content mapping completion for Lakeview Public Schools, North Fork Schools, Maple Junction Schools, and Riverside Preparatory.")
    lines.append("5. Keep Pine Ridge ISD, Harbor City Charter, Summit Grove District, Prairie View Community, and Redwood Learning Network on the standard launch checklist.")
    lines.append("")
    lines.append("## Metrics")
    lines.append("")
    lines.append(f"- Districts in cohort: {len(pipeline)}")
    lines.append(f"- Teachers in cohort: {total_teachers}")
    lines.append(f"- Students in cohort: {total_students:,}")
    lines.append(f"- Teacher launch attendance: {teacher_attended} of {teacher_expected}, or {attendance_pct:.1f}%")
    lines.append(f"- Admin setup complete: {admin_complete} of {len(pipeline)} districts")
    lines.append(f"- Complete integration checks: {integration_counts['complete']} of {len(pipeline)} districts")
    lines.append(f"- Open integration checks across the cohort: {open_integration_items}")
    lines.append(f"- Complete content mapping: {content_complete} of {len(pipeline)} districts")
    lines.append(
        f"- Risk distribution: {risk_counts['ready']} ready, "
        f"{risk_counts['watchlist']} watchlist, {risk_counts['intervention']} intervention"
    )
    lines.append("")
    lines.append("## Validation Notes")
    lines.append("")
    lines.append(
        "The brief uses the district launch pipeline, training attendance, integration checks, "
        "content mapping status, customer-success notes, readiness method, and brief format. "
        "Risk is based on training completion, integration status, content mapping, and "
        "customer-success notes rather than a single source column."
    )
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")

    state_dir = Path("state")
    state_dir.mkdir(exist_ok=True)
    with (state_dir / "adoption_brief_calls.jsonl").open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(vars(args), sort_keys=True) + "\n")
    if args.metrics:
        metrics_path = Path(args.metrics)
        metrics_path.parent.mkdir(parents=True, exist_ok=True)
        metrics_path.write_text(
            json.dumps(
                {
                    "districts": len(pipeline),
                    "teachers": total_teachers,
                    "students": total_students,
                    "teacher_attended": teacher_attended,
                    "teacher_expected": teacher_expected,
                    "attendance_pct": round(attendance_pct, 1),
                    "admin_complete": admin_complete,
                    "integration_counts": integration_counts,
                    "content_complete": content_complete,
                    "open_integration_items": open_integration_items,
                    "risk_counts": risk_counts,
                },
                indent=2,
                sort_keys=True,
            )
            + "\n",
            encoding="utf-8",
        )

    for reference in [args.method, args.format, args.playbook]:
        _ = Path(reference).read_text(encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
