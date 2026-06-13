#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True)
    parser.add_argument("--index", required=True)
    parser.add_argument("--custody-note", required=True)
    parser.add_argument("--manifest", required=True)
    args = parser.parse_args()

    root = Path(args.root)
    results = Path(args.index).parent
    results.mkdir(parents=True, exist_ok=True)

    scope = load_csv(root / "records" / "packet_scope.csv")[0]
    exhibits = load_csv(root / "records" / "exhibit_register.csv")
    custody = {
        row["exhibit_id"]: row
        for row in load_csv(root / "records" / "custody_table.csv")
    }

    lines = [
        "# Public Evidence Index",
        "",
        f"Matter: {scope['matter']}",
        f"Matter code: {scope['matter_code']}",
        f"Packet label: {scope['packet_label']}",
        "",
        "## Packet Purpose",
        scope["packet_purpose"],
        "",
        "## Reviewed Exhibits",
        "",
        "| Exhibit | Title | Custodian | Status | Supports |",
        "|---|---|---|---|---|",
    ]
    followups = []
    for row in exhibits:
        c = custody[row["exhibit_id"]]
        lines.append(
            "| {exhibit_id} | {title} | {custodian} | {status} | {summary} |".format(
                exhibit_id=row["exhibit_id"],
                title=row["title"],
                custodian=c["custodian"],
                status=c["review_status"],
                summary=row["public_summary"],
            )
        )
        if c["review_status"] != "ready":
            followups.append((row, c))
    lines.extend(["", "## Public Follow-up Items"])
    if followups:
        for row, c in followups:
            lines.append(f"- {row['exhibit_id']}: {c['custody_note']}")
    else:
        lines.append("- No public-response follow-up items are recorded.")
    Path(args.index).write_text("\n".join(lines) + "\n", encoding="utf-8")

    custodians = sorted({custody[row["exhibit_id"]]["custodian"] for row in exhibits})
    note_lines = [
        "# Custody Note",
        "",
        f"Source tables: records/packet_scope.csv, records/exhibit_register.csv, records/custody_table.csv.",
        f"Reviewed exhibit count: {len(exhibits)}.",
        f"Disclosure status: public packet materials.",
        "Custodians represented: " + "; ".join(custodians) + ".",
        "",
        "## Follow-up",
    ]
    if followups:
        for row, c in followups:
            note_lines.append(f"- {row['exhibit_id']} ({row['title']}): {c['custody_note']}")
    else:
        note_lines.append("- No follow-up items recorded.")
    Path(args.custody_note).write_text("\n".join(note_lines) + "\n", encoding="utf-8")

    manifest = {
        "sources": [
            "harbor_evidence_review/README.md",
            "harbor_evidence_review/docs/handoff_request.md",
            "harbor_evidence_review/docs/records_closeout_notes.md",
            "harbor_evidence_review/docs/public_packet_style.md",
            "harbor_evidence_review/records/packet_scope.csv",
            "harbor_evidence_review/records/exhibit_register.csv",
            "harbor_evidence_review/records/custody_table.csv",
        ] + [
            "harbor_evidence_review/" + row["file_path"]
            for row in exhibits
        ],
        "generated_outputs": [
            "results/public_evidence_index.md",
            "results/custody_note.md",
            "results/source_manifest.json",
        ],
    }
    Path(args.manifest).write_text(json.dumps(manifest, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
