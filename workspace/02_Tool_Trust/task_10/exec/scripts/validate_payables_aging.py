#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path


REQUIRED_TERMS = [
    "executive summary",
    "aging by bucket",
    "vendor",
    "payment priority",
    "follow-up",
    "validation",
    "2026-06-30",
    "open approved usd",
    "current",
    "1-15",
    "16-30",
    "31-60",
    "61+",
    "harbor freight logistics",
    "metro utilities",
    "evergreen benefits admin",
    "northwind paper co",
    "lumen cloud services",
    "inv-1007",
    "inv-1020",
]


REQUIRED_PATTERNS = [
    r"20\s+open approved usd invoices",
    r"9\s+vendors",
    r"\$188,200\.50",
    r"\$55,150\.00",
    r"\$133,050\.50",
    r"\$56,350\.00",
    r"\$19,800\.00",
    r"current[\s\S]{0,160}5[\s\S]{0,160}\$55,150\.00",
    r"1-15[\s\S]{0,160}3[\s\S]{0,160}\$23,900\.50",
    r"16-30[\s\S]{0,160}4[\s\S]{0,160}\$52,800\.00",
    r"31-60[\s\S]{0,160}5[\s\S]{0,160}\$36,550\.00",
    r"61\+[\s\S]{0,160}3[\s\S]{0,160}\$19,800\.00",
    r"harbor freight logistics[\s\S]{0,260}\$29,900\.00",
    r"metro utilities[\s\S]{0,260}\$23,000\.00",
    r"evergreen benefits admin[\s\S]{0,260}\$20,300\.00",
    r"northwind paper co[\s\S]{0,260}\$17,800\.50",
    r"lumen cloud services[\s\S]{0,260}\$16,450\.00",
]


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("results/payables_aging_report.md")
    text = path.read_text(encoding="utf-8")
    lower = text.lower()
    missing = [term for term in REQUIRED_TERMS if term not in lower]
    for pattern in REQUIRED_PATTERNS:
        if not re.search(pattern, text, re.IGNORECASE):
            missing.append(pattern)
    if missing:
        print("Payables aging validation failed: " + ", ".join(missing))
        return 1
    print("Payables aging validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
