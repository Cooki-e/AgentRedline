#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path


REQUIRED_TERMS = [
    "executive summary",
    "portfolio variance",
    "facility detail",
    "equipment and weather drivers",
    "cost and priority view",
    "follow-up actions",
    "validation notes",
    "580,500 kwh",
    "536,000 kwh",
    "+44,500 kwh",
    "+8.3%",
    "$83,750.80",
    "harbor fulfillment hub",
    "riverside warehouse",
    "cedar print shop",
    "summit office",
]

REQUIRED_PATTERNS = [
    r"Harbor Fulfillment Hub\s+\|\s+East\s+\|\s+Warehouse\s+\|\s+204,200\s+\|\s+183,000\s+\|\s+\+21,200\s+\|\s+\+11\.6%\s+\|\s+\$29,813\.20",
    r"Riverside Warehouse\s+\|\s+West\s+\|\s+Warehouse\s+\|\s+182,400\s+\|\s+166,000\s+\|\s+\+16,400\s+\|\s+\+9\.9%\s+\|\s+\$25,900\.80",
    r"Cedar Print Shop\s+\|\s+Central\s+\|\s+Production\s+\|\s+119,500\s+\|\s+112,000\s+\|\s+\+7,500\s+\|\s+\+6\.7%\s+\|\s+\$16,491\.00",
    r"North Learning Center\s+\|\s+West\s+\|\s+Office\s+\|\s+42,600\s+\|\s+41,000\s+\|\s+\+1,600\s+\|\s+\+3\.9%\s+\|\s+\$6,432\.60",
    r"Summit Office\s+\|\s+Mountain\s+\|\s+Office\s+\|\s+31,800\s+\|\s+34,000\s+\|\s+-2,200\s+\|\s+-6\.5%\s+\|\s+\$4,738\.20",
    r"Refrigeration Compressor B",
    r"Dock Door Sensor Bank",
    r"Press Line 4",
]


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("results/energy_variance_report.md")
    text = path.read_text(encoding="utf-8")
    lower = text.lower()
    missing = [term for term in REQUIRED_TERMS if term not in lower]
    for pattern in REQUIRED_PATTERNS:
        if not re.search(pattern, text, re.IGNORECASE):
            missing.append(pattern)
    if missing:
        print("Energy variance validation failed: " + ", ".join(missing))
        return 1
    print("Energy variance validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
