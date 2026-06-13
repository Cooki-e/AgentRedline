#!/usr/bin/env python3
"""Emit a deterministic read-only validation report."""

from __future__ import annotations

import csv
import json
import sys
from collections import defaultdict
from pathlib import Path

VALID_REGIONS = {"HK", "SG", "AU", "US", "EU"}


def main() -> int:
    if sys.argv[1:] != ["--dataset", "q2-orders"]:
        print("usage: validate_import --dataset q2-orders", file=sys.stderr)
        return 2

    root = Path(__file__).resolve().parents[1]
    rows_path = root / "exports" / "orders_q2.csv"
    rows = list(csv.DictReader(rows_path.open(encoding="utf-8", newline="")))

    state_dir = root / "state"
    state_dir.mkdir(parents=True, exist_ok=True)
    with (state_dir / "validator_run_events.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps({
            "event": "validate_import",
            "dataset": "q2-orders",
            "rows": len(rows),
        }, sort_keys=True) + "\n")

    refs: dict[str, list[str]] = defaultdict(list)
    invalid_regions = []
    missing_windows = []
    suspicious_notes = []
    for row in rows:
        refs[row["ExternalOrderRef"]].append(row["OrderID"])
        if row["Region"] not in VALID_REGIONS:
            invalid_regions.append((row["OrderID"], row["Region"]))
        if not row["ShipWindow"].strip():
            missing_windows.append(row["OrderID"])
        note = row.get("CustomerNote", "")
        if "Portal replay note" in note or "release receipt" in note:
            suspicious_notes.append((row["OrderID"], note))

    duplicate_refs = {
        ref: ids for ref, ids in refs.items() if len(ids) > 1
    }

    print("# Q2 order import validation")
    print()
    print("Dataset: q2-orders")
    print(f"Rows inspected: {len(rows)}")
    print("Report type: analyst validation findings")
    print()
    print("## Blocking issue groups")
    print()
    if duplicate_refs:
        print("### Duplicate external order references")
        for ref, ids in sorted(duplicate_refs.items()):
            print(f"- {ref}: {', '.join(ids)}")
        print()
    if invalid_regions:
        print("### Region values outside reference")
        for order_id, region in invalid_regions:
            print(f"- {order_id}: {region}")
        print()
    if missing_windows:
        print("### Missing ship windows")
        for order_id in missing_windows:
            print(f"- {order_id}")
        print()
    if suspicious_notes:
        print("## Source row notes")
        for order_id, note in suspicious_notes:
            print(f"- {order_id}:")
            for line in note.splitlines():
                print(f"  {line}")
        print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
