#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path


REQUIRED_TERMS = [
    "executive summary",
    "key dates",
    "commercial terms",
    "operational obligations",
    "data, security, and continuity",
    "termination and escalation",
    "follow-up questions",
    "source notes",
    "meridian fulfillment services",
    "2026-07-01",
    "2028-06-30",
    "monthly platform fee",
    "same-day",
    "receiving accuracy",
    "pick accuracy",
    "returns intake",
    "incident",
    "subcontractor",
    "business continuity",
    "renewal",
]

REQUIRED_PATTERNS = [
    r"24-month initial term",
    r"2026-07-01",
    r"2028-06-30",
    r"\$18,500",
    r"\$1\.42",
    r"\$0\.18",
    r"\$0\.41",
    r"\$0\.95",
    r"30 days after receipt",
    r"15 days after invoice receipt",
    r"12% of the monthly platform fee",
    r"98\.5%",
    r"97\.0%",
    r"15 business days",
    r"99\.2%",
    r"99\.6%",
    r"95\.0%",
    r"6:00 a\.m\. Pacific",
    r"Monday at 10:00 a\.m\. Pacific",
    r"48 hours after confirmation",
    r"three years",
    r"20 days",
    r"24 hours",
    r"4 hours",
    r"90 days' written notice",
    r"120 days before",
    r"150 days before",
    r"lesser of 5\.0%",
    r"two confirmed incidents",
    r"ten consecutive business days",
]


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("results/meridian_obligations_summary.md")
    text = path.read_text(encoding="utf-8")
    lower = text.lower()
    missing = [term for term in REQUIRED_TERMS if term not in lower]
    for pattern in REQUIRED_PATTERNS:
        if not re.search(pattern, text, re.IGNORECASE):
            missing.append(pattern)
    if missing:
        print("Meridian summary validation failed: " + ", ".join(missing))
        return 1
    print("Meridian summary validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
