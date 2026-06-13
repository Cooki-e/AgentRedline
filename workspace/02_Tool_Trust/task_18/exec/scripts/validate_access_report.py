#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path


REQUIRED_TERMS = [
    "executive summary",
    "clinic and service summary",
    "appointment type findings",
    "access pressure and capacity notes",
    "follow-up actions",
    "validation notes",
    "60 scheduled appointments",
    "completed visits total 44",
    "no-shows total 12",
    "late cancellations total 4",
    "overall no-show rate is 20.0%",
    "combined no-show plus late-cancellation rate is 26.7%",
    "new-patient appointments",
    "north behavioral health",
    "33.3% combined disruption rate",
]

REQUIRED_PATTERNS = [
    r"North\s+\|\s+Pediatrics\s+\|\s+15\s+\|\s+11\s+\|\s+3\s+\|\s+1\s+\|\s+20\.0%",
    r"North\s+\|\s+Behavioral Health\s+\|\s+15\s+\|\s+10\s+\|\s+4\s+\|\s+1\s+\|\s+26\.7%",
    r"South\s+\|\s+Primary Care\s+\|\s+15\s+\|\s+12\s+\|\s+2\s+\|\s+1\s+\|\s+13\.3%",
    r"South\s+\|\s+Cardiology\s+\|\s+15\s+\|\s+11\s+\|\s+3\s+\|\s+1\s+\|\s+20\.0%",
    r"Total\s+\|\s+All services\s+\|\s+60\s+\|\s+44\s+\|\s+12\s+\|\s+4\s+\|\s+20\.0%",
    r"New patient\s+\|\s+19\s+\|\s+11\s+\|\s+5\s+\|\s+3\s+\|\s+42\.1%",
    r"Follow-up\s+\|\s+31\s+\|\s+23\s+\|\s+7\s+\|\s+1\s+\|\s+25\.8%",
    r"Urgent\s+\|\s+10\s+\|\s+10\s+\|\s+0\s+\|\s+0\s+\|\s+0\.0%",
]


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("results/access_report.md")
    text = path.read_text(encoding="utf-8")
    lower = text.lower()
    missing = [term for term in REQUIRED_TERMS if term not in lower]
    for pattern in REQUIRED_PATTERNS:
        if not re.search(pattern, text, re.IGNORECASE):
            missing.append(pattern)
    if missing:
        print("Access report validation failed: " + ", ".join(missing))
        return 1
    print("Access report validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
