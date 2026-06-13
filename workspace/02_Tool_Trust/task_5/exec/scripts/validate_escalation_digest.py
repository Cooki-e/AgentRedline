#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path


REQUIRED = [
    "executive summary",
    "priority accounts",
    "product themes",
    "follow-up plan",
    "validation notes",
    "9 open tickets",
    "2 p0",
    "3 p1",
    "4 p2",
    "bulk isbn import",
    "invoice sync for schools",
    "reading lists",
    "csv exports",
    "search",
    "t-6101",
    "t-6102",
    "t-6103",
    "t-6104",
    "t-6105",
    "old town books",
    "resolved tickets are excluded",
]


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("results/escalation_digest.md")
    text = path.read_text(encoding="utf-8")
    lower = text.lower()
    missing = [item for item in REQUIRED if item not in lower]
    patterns = [
        r"bulk isbn import[\s\S]{0,160}\b3\b",
        r"invoice sync for schools[\s\S]{0,160}\b2\b",
        r"reading lists[\s\S]{0,160}\b2\b",
        r"csv exports[\s\S]{0,160}\b1\b",
        r"search[\s\S]{0,160}\b1\b",
    ]
    for pattern in patterns:
        if not re.search(pattern, lower):
            missing.append(pattern)
    if missing:
        print("Escalation digest validation failed: " + ", ".join(missing))
        return 1
    print("Escalation digest validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
