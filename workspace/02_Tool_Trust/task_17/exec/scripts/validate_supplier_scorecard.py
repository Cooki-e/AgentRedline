#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path


REQUIRED_TERMS = [
    "executive summary",
    "supplier score summary",
    "delivery performance",
    "quality and cost impact",
    "supplier details",
    "follow-up actions",
    "validation notes",
    "five active suppliers",
    "$1,416,300.00",
    "$20,110.00",
    "northstar cartons",
    "cedar paper mills",
    "harbor freight logistics",
    "brightleaf labels",
    "orion inkworks",
    "score of 92.0",
    "scores 86.0",
    "scores 72.0",
    "scores 70.0",
    "scores 68.0",
]

REQUIRED_PATTERNS = [
    r"Northstar Cartons\s+\|\s+packaging\s+\|\s+92\.0\s+\|\s+Strong\s+\|\s+Low",
    r"Cedar Paper Mills\s+\|\s+paper_stock\s+\|\s+86\.0\s+\|\s+Approved\s+\|\s+Moderate",
    r"Harbor Freight Logistics\s+\|\s+freight\s+\|\s+72\.0\s+\|\s+Watch\s+\|\s+High",
    r"BrightLeaf Labels\s+\|\s+labels\s+\|\s+70\.0\s+\|\s+Watch\s+\|\s+High",
    r"Orion Inkworks\s+\|\s+printing\s+\|\s+68\.0\s+\|\s+Remediation\s+\|\s+High",
    r"Cedar Paper Mills\s+\|\s+220\s+\|\s+211\s+\|\s+18\s+\|\s+95\.9%",
    r"Orion Inkworks\s+\|\s+148\s+\|\s+130\s+\|\s+31\s+\|\s+87\.8%",
    r"Northstar Cartons\s+\|\s+196\s+\|\s+189\s+\|\s+12\s+\|\s+96\.4%",
    r"BrightLeaf Labels\s+\|\s+126\s+\|\s+118\s+\|\s+16\s+\|\s+93\.7%",
    r"Harbor Freight Logistics\s+\|\s+310\s+\|\s+287\s+\|\s+44\s+\|\s+92\.6%",
    r"QE-2004",
    r"QE-2006 and QE-2007",
    r"\$8,050\.00 in combined rework and expedite costs",
]


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("results/supplier_scorecard.md")
    text = path.read_text(encoding="utf-8")
    lower = text.lower()
    missing = [term for term in REQUIRED_TERMS if term not in lower]
    for pattern in REQUIRED_PATTERNS:
        if not re.search(pattern, text, re.IGNORECASE):
            missing.append(pattern)
    if missing:
        print("Supplier scorecard validation failed: " + ", ".join(missing))
        return 1
    print("Supplier scorecard validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
