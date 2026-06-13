#!/usr/bin/env python3
from __future__ import annotations

import csv
import sys
from pathlib import Path


FIELDNAMES = [
    "stream_id",
    "owner",
    "window_start",
    "window_end",
    "expected_count",
    "observed_count",
    "status",
    "note",
]


def parse_stream(path: Path) -> dict[str, str]:
    with path.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        raise SystemExit(f"no rows in {path}")
    row = rows[0]
    expected = int(row["expected_count"])
    observed = int(row["observed_count"])
    status = "pass" if expected == observed else "review"
    note = (
        "Observed count matches expected count."
        if status == "pass"
        else f"Observed count {observed} differs from expected count {expected}."
    )
    return {
        "stream_id": row["stream_id"],
        "owner": row["owner"],
        "window_start": row["window_start"],
        "window_end": row["window_end"],
        "expected_count": str(expected),
        "observed_count": str(observed),
        "status": status,
        "note": note,
    }


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: parse_stream.py <stream-csv>")
    out = csv.DictWriter(sys.stdout, fieldnames=FIELDNAMES)
    out.writerow(parse_stream(Path(sys.argv[1])))


if __name__ == "__main__":
    main()
