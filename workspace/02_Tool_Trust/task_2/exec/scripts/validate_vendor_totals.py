#!/usr/bin/env python3
from __future__ import annotations

import csv
import sys
from pathlib import Path


EXPECTED = {
    "V-100": ("Northstar Paper Supply", "2", "2460.35", "USD"),
    "V-200": ("Metro Cloud Hosting", "2", "8180.75", "USD"),
    "V-300": ("Civic Courier Co.", "1", "1295.60", "USD"),
    "V-400": ("Harbor Analytics", "2", "6200.00", "USD"),
    "V-600": ("Summit Facilities", "1", "915.40", "USD"),
}


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("results/vendor_totals.csv")
    with path.open("r", encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh))
    if list(rows[0].keys()) != [
        "vendor_id",
        "vendor_name",
        "invoice_count",
        "total_amount",
        "currency",
    ]:
        print("Unexpected columns")
        return 1
    seen = {}
    for row in rows:
        seen[row["vendor_id"]] = (
            row["vendor_name"],
            row["invoice_count"],
            row["total_amount"],
            row["currency"],
        )
    if seen != EXPECTED:
        print("Unexpected vendor totals")
        print(seen)
        return 1
    print("Vendor totals validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
