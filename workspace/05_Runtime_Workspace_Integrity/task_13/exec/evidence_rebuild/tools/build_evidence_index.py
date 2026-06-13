#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
from pathlib import Path


FIELDNAMES = [
    "exhibit_id",
    "source_file",
    "source_type",
    "matter",
    "custodian",
    "review_status",
    "note",
]


def parse_exhibit(path: Path) -> dict[str, str]:
    values = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip()
    missing = [field for field in FIELDNAMES if field not in values]
    if missing:
        raise SystemExit(f"{path} missing fields: {', '.join(missing)}")
    return {field: values[field] for field in FIELDNAMES}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    input_dir = Path(args.input)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    rows = [parse_exhibit(path) for path in sorted(input_dir.glob("*.txt"))]
    with output.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    main()
