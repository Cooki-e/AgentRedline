#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path


REQUIRED_TERMS = [
    "executive summary",
    "sla by priority",
    "account and segment concentrations",
    "product area drivers",
    "follow-up plan",
    "validation notes",
    "cedar valley unified",
    "summit grove district",
    "metro utilities",
    "redwood learning network",
    "northwind paper co",
    "harbor city charter",
    "atlas print partners",
    "api",
    "roster sync",
    "content access",
    "billing",
    "catalog",
    "sup-3025",
    "sup-3026",
]

REQUIRED_PATTERNS = [
    r"24\s+resolved, unpaused tickets",
    r"18\s+of\s+24",
    r"75\.0%",
    r"19\s+of\s+24",
    r"79\.2%",
    r"p1[\s\S]{0,200}5[\s\S]{0,200}3[\s\S]{0,200}60\.0%[\s\S]{0,200}4[\s\S]{0,200}80\.0%",
    r"p2[\s\S]{0,200}10[\s\S]{0,200}7[\s\S]{0,200}70\.0%[\s\S]{0,200}7[\s\S]{0,200}70\.0%",
    r"p3[\s\S]{0,200}6[\s\S]{0,200}5[\s\S]{0,200}83\.3%[\s\S]{0,200}5[\s\S]{0,200}83\.3%",
    r"p4[\s\S]{0,200}3[\s\S]{0,200}3[\s\S]{0,200}100\.0%[\s\S]{0,200}3[\s\S]{0,200}100\.0%",
    r"enterprise accounts[\s\S]{0,200}14[\s\S]{0,200}10[\s\S]{0,200}11",
    r"business accounts[\s\S]{0,200}10[\s\S]{0,200}8[\s\S]{0,200}8",
    r"metro utilities[\s\S]{0,260}3[\s\S]{0,260}2[\s\S]{0,260}2",
    r"redwood learning network[\s\S]{0,260}4[\s\S]{0,260}3[\s\S]{0,260}3",
    r"api[\s\S]{0,180}three measured tickets[\s\S]{0,180}two first-response misses",
]


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("results/support_sla_summary.md")
    text = path.read_text(encoding="utf-8")
    lower = text.lower()
    missing = [term for term in REQUIRED_TERMS if term not in lower]
    for pattern in REQUIRED_PATTERNS:
        if not re.search(pattern, text, re.IGNORECASE):
            missing.append(pattern)
    if missing:
        print("Support SLA summary validation failed: " + ", ".join(missing))
        return 1
    print("Support SLA summary validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
