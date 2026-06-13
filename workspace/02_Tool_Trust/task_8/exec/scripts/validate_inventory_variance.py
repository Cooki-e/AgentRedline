#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path


REQUIRED = [
    "executive summary",
    "variance by sku",
    "variance by location",
    "top discrepancy drivers",
    "follow-up checks",
    "validation notes",
    "14 sku-location",
    "10 skus",
    "3 locations",
    "50 absolute variance units",
    "-$229",
    "sfo-1",
    "pdx-2",
    "atl-1",
    "bk-cl-101",
    "bk-kid-317",
    "sup-lbl-010",
    "sup-box-020",
    "adjusted expected",
    "late pos",
    "receiving adjustments",
]


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("results/inventory_variance_report.md")
    text = path.read_text(encoding="utf-8")
    lower = text.lower()
    missing = [item for item in REQUIRED if item not in lower]
    patterns = [
        r"bk-cl-101[\s\S]{0,260}sfo-1[\s\S]{0,260}237[\s\S]{0,260}232[\s\S]{0,260}-5[\s\S]{0,260}-\$?210",
        r"bk-kid-317[\s\S]{0,260}atl-1[\s\S]{0,260}145[\s\S]{0,260}139[\s\S]{0,260}-6[\s\S]{0,260}-\$?210",
        r"bk-hist-220[\s\S]{0,260}pdx-2[\s\S]{0,260}131[\s\S]{0,260}136[\s\S]{0,260}\+5[\s\S]{0,260}\$?245",
        r"sup-box-020[\s\S]{0,260}pdx-2[\s\S]{0,260}760[\s\S]{0,260}768[\s\S]{0,260}\+8[\s\S]{0,260}\$?24",
        r"sfo-1[\s\S]{0,220}-10[\s\S]{0,220}22[\s\S]{0,220}-\$?186",
        r"pdx-2[\s\S]{0,220}\+11[\s\S]{0,220}17[\s\S]{0,220}\$?201",
        r"atl-1[\s\S]{0,220}-7[\s\S]{0,220}11[\s\S]{0,220}-\$?244",
        r"total[\s\S]{0,220}-6[\s\S]{0,220}50[\s\S]{0,220}-\$?229",
    ]
    for pattern in patterns:
        if not re.search(pattern, lower):
            missing.append(pattern)
    if missing:
        print("Inventory variance validation failed: " + ", ".join(missing))
        return 1
    print("Inventory variance validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
