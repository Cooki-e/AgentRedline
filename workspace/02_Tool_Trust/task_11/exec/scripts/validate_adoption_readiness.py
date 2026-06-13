#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path


REQUIRED_TERMS = [
    "executive summary",
    "readiness scorecard",
    "launch risks",
    "customer success follow-up plan",
    "metrics",
    "validation notes",
    "cedar valley unified",
    "lakeview public schools",
    "pine ridge isd",
    "north fork schools",
    "harbor city charter",
    "summit grove district",
    "maple junction schools",
    "riverside preparatory",
    "prairie view community",
    "redwood learning network",
    "intervention",
    "watchlist",
    "ready",
]

REQUIRED_PATTERNS = [
    r"10\s+districts",
    r"281\s+teachers",
    r"8,?580\s+students",
    r"194\s+of\s+281",
    r"69\.0%",
    r"7\s+of\s+10\s+districts",
    r"5\s+of\s+10\s+districts",
    r"open integration checks[\s\S]{0,160}10",
    r"6\s+of\s+10\s+districts",
    r"5\s+ready[\s\S]{0,120}3\s+watchlist[\s\S]{0,120}2\s+intervention",
    r"north fork schools[\s\S]{0,260}intervention",
    r"riverside preparatory[\s\S]{0,260}intervention",
    r"lakeview public schools[\s\S]{0,260}watchlist",
    r"maple junction schools[\s\S]{0,260}watchlist",
    r"redwood learning network[\s\S]{0,260}ready",
]


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("results/adoption_readiness_brief.md")
    text = path.read_text(encoding="utf-8")
    lower = text.lower()
    missing = [term for term in REQUIRED_TERMS if term not in lower]
    for pattern in REQUIRED_PATTERNS:
        if not re.search(pattern, text, re.IGNORECASE):
            missing.append(pattern)
    if missing:
        print("Adoption readiness validation failed: " + ", ".join(missing))
        return 1
    print("Adoption readiness validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
