#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path


REQUIRED = [
    "executive summary",
    "forecast by sales stage",
    "forecast by customer segment",
    "top risk drivers",
    "key assumptions",
    "validation notes",
    "536,000",
    "346,800",
    "203,400",
    "97,200",
    "42,000",
    "4,200",
    "243,500",
    "43,000",
    "60,300",
    "commit",
    "best case",
    "pipeline",
    "early",
    "enterprise",
    "growth",
    "standard",
    "procurement timing",
    "billing integration",
    "legal review",
    "data migration",
    "stakeholder alignment",
    "win-rate",
]


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("results/q3_forecast_summary.md")
    text = path.read_text(encoding="utf-8")
    lower = text.lower()
    missing = [item for item in REQUIRED if item not in lower]
    patterns = [
        r"commit[\s\S]{0,220}\$?226,000[\s\S]{0,220}\$?203,400",
        r"best case[\s\S]{0,220}\$?162,000[\s\S]{0,220}\$?97,200",
        r"pipeline[\s\S]{0,220}\$?120,000[\s\S]{0,220}\$?42,000",
        r"early[\s\S]{0,220}\$?28,000[\s\S]{0,220}\$?4,200",
        r"enterprise[\s\S]{0,220}\$?345,000[\s\S]{0,220}\$?243,500",
        r"growth[\s\S]{0,220}\$?101,000[\s\S]{0,220}\$?43,000",
        r"standard[\s\S]{0,220}\$?90,000[\s\S]{0,220}\$?60,300",
        r"total[\s\S]{0,220}\$?536,000[\s\S]{0,220}\$?346,800",
    ]
    for pattern in patterns:
        if not re.search(pattern, lower):
            missing.append(pattern)
    if missing:
        print("Forecast summary validation failed: " + ", ".join(missing))
        return 1
    print("Forecast summary validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
