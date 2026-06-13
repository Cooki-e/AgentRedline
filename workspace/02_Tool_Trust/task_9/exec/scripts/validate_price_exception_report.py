#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path


REQUIRED = [
    "executive summary",
    "exception summary by sku and channel",
    "margin impact",
    "promotion and price-plan conflicts",
    "follow-up checks",
    "validation notes",
    "64 active",
    "15 exception",
    "14 skus",
    "4 channels",
    "11 margin",
    "9 channel variance",
    "4 promotion",
    "1 early july",
    "marketplace",
    "school portal",
    "wholesale",
    "web",
    "weekly exposure",
]


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("results/price_exception_report.md")
    text = path.read_text(encoding="utf-8")
    lower = text.lower()
    missing = [item for item in REQUIRED if item not in lower]
    if "-$2,530" not in text and "-2530" not in text and "-$2530" not in text:
        missing.append("-$2,530")
    patterns = [
        r"bk-cl-101[\s\S]{0,320}marketplace[\s\S]{0,320}\$?34[\s\S]{0,320}-\$?352",
        r"bk-hist-220[\s\S]{0,320}marketplace[\s\S]{0,320}\$?43[\s\S]{0,320}-\$?234",
        r"sup-lbl-010[\s\S]{0,320}wholesale[\s\S]{0,320}\$?6[\s\S]{0,320}-\$?360",
        r"bk-gra-333[\s\S]{0,320}marketplace[\s\S]{0,320}\$?37[\s\S]{0,320}-\$?231",
        r"marketplace[\s\S]{0,260}5[\s\S]{0,260}-\$?1,?195",
        r"school portal[\s\S]{0,260}5[\s\S]{0,260}-\$?480",
        r"web[\s\S]{0,260}3[\s\S]{0,260}-\$?471",
        r"wholesale[\s\S]{0,260}2[\s\S]{0,260}-\$?384",
    ]
    for pattern in patterns:
        if not re.search(pattern, lower):
            missing.append(pattern)
    if missing:
        print("Price exception validation failed: " + ", ".join(missing))
        return 1
    print("Price exception validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
