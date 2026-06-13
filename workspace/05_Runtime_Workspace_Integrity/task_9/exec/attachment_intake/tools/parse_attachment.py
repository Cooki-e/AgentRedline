#!/usr/bin/env python3
from __future__ import annotations

import csv
import sys
from pathlib import Path


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: parse_attachment.py <csv-file>")
    path = Path(sys.argv[1])
    with path.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        raise SystemExit(f"no rows in {path}")

    declared = float(rows[0]["declared_total"])
    parsed = sum(float(row["amount"]) for row in rows)
    status = "pass" if abs(declared - parsed) < 0.005 else "review"
    note = (
        "Declared total matches parsed line items."
        if status == "pass"
        else f"Declared total {declared:.2f} differs from parsed total {parsed:.2f}."
    )
    out = csv.DictWriter(
        sys.stdout,
        fieldnames=[
            "file_name",
            "sender",
            "received_date",
            "attachment_type",
            "declared_total",
            "parsed_total",
            "status",
            "note",
        ],
    )
    out.writerow({
        "file_name": path.name,
        "sender": rows[0]["sender"],
        "received_date": rows[0]["received_date"],
        "attachment_type": rows[0]["attachment_type"],
        "declared_total": f"{declared:.2f}",
        "parsed_total": f"{parsed:.2f}",
        "status": status,
        "note": note,
    })


if __name__ == "__main__":
    main()
