#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
import sys
from pathlib import Path


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: write_exception_register.py <dependency_policy_summary.json>")
    data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    rows = [
        item
        for item in data["dependencies"]
        if item.get("policy_status") == "review"
    ]
    fieldnames = [
        "package",
        "owner",
        "component",
        "policy_status",
        "reason",
        "recommended_action",
    ]
    writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames)
    writer.writeheader()
    for row in rows:
        writer.writerow({key: row.get(key, "") for key in fieldnames})


if __name__ == "__main__":
    main()
