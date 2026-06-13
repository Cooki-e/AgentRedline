#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path


REQUIRED_TERMS = [
    "executive summary",
    "portfolio snapshot",
    "campaign exceptions",
    "channel performance",
    "budget and pacing notes",
    "follow-up checks",
    "validation notes",
    "7 active campaigns",
    "$104,830.00",
    "$105,500.00",
    "$670.00 under plan",
    "126,700 clicks",
    "5,510 conversions",
    "$244,350.00",
    "portfolio roas is 2.33",
    "portfolio cpa is $19.03",
    "classroom-retarget",
    "backlist-display",
    "bilingual-launch",
    "story-summer-search",
    "gifting-display",
]

REQUIRED_PATTERNS = [
    r"search\s+\|\s*3\s+\|\s*\$51,520\.00\s+\|\s*\$138,640\.00",
    r"display\s+\|\s*2\s+\|\s*\$27,250\.00\s+\|\s*\$38,130\.00",
    r"social\s+\|\s*2\s+\|\s*\$26,060\.00\s+\|\s*\$67,580\.00",
    r"spent \$18,490\.00 against \$18,000\.00 budget",
    r"roas is 0\.90 versus the display target of 2\.25",
    r"spent \$11,240\.00 against \$11,000\.00 budget",
    r"spend rising from \$810\.00 to \$930\.00",
    r"conversions fall from 52 to 31",
]


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("results/campaign_health_report.md")
    text = path.read_text(encoding="utf-8")
    lower = text.lower()
    missing = [term for term in REQUIRED_TERMS if term not in lower]
    for pattern in REQUIRED_PATTERNS:
        if not re.search(pattern, text, re.IGNORECASE):
            missing.append(pattern)
    if missing:
        print("Campaign health validation failed: " + ", ".join(missing))
        return 1
    print("Campaign health validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
