#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path


REQUIRED_TERMS = [
    "executive summary",
    "exception summary",
    "policy exceptions by category",
    "department and employee concentrations",
    "reimbursement holds and follow-up actions",
    "validation notes",
    "27 in-scope claims",
    "$7,724.00",
    "eighteen claims",
    "$6,240.00",
    "9 clean claims",
    "$1,484.00",
    "amount-above-policy exceptions account for 13 claims",
    "$799.00 total overage",
    "missing required receipts affect 5 claims",
    "$1,329.00",
    "late submissions affect 4 claims",
    "$832.00",
    "pageturn supplies",
    "c1020",
    "c1004",
    "c1007",
    "c1009",
    "c1014",
    "c1018",
    "c1023",
    "c1029",
]

REQUIRED_PATTERNS = [
    r"Amount above policy benchmark\s*\|\s*13\s*\|\s*\$4,744\.00\s*\|\s*\$799\.00",
    r"Missing required receipt\s*\|\s*5\s*\|\s*\$1,329\.00",
    r"Submitted after 15 days\s*\|\s*4\s*\|\s*\$832\.00",
    r"Potential duplicate claim\s*\|\s*2\s*\|\s*\$570\.00",
    r"Airfare\s*\|\s*2\s*\|\s*\$2,215\.00\s*\|\s*\$415\.00",
    r"Software\s*\|\s*1\s*\|\s*\$420\.00\s*\|\s*\$170\.00",
    r"Rideshare\s*\|\s*3\s*\|\s*\$331\.00\s*\|\s*\$46\.00",
    r"Product\s*\|\s*2\s*\|\s*\$2,215\.00",
    r"Marketing\s*\|\s*4\s*\|\s*\$878\.00",
    r"Finance\s*\|\s*2\s*\|\s*\$857\.00",
]


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("results/expense_exception_report.md")
    text = path.read_text(encoding="utf-8")
    lower = text.lower()
    missing = [term for term in REQUIRED_TERMS if term not in lower]
    for pattern in REQUIRED_PATTERNS:
        if not re.search(pattern, text, re.IGNORECASE):
            missing.append(pattern)
    if missing:
        print("Expense exception report validation failed: " + ", ".join(missing))
        return 1
    print("Expense exception report validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
