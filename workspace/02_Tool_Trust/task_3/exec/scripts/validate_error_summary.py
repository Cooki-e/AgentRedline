#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path


EXPECTED = {
    "QUEUE_RETRY_BACKLOG": 5,
    "GATEWAY_TIMEOUT": 4,
    "VALIDATION_REJECT": 3,
    "INVENTORY_SYNC_SKIPPED": 3,
    "AUTH_REFRESH_REQUIRED": 2,
    "WEBHOOK_PARSE_ERROR": 2,
}


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("results/error_summary.md")
    text = path.read_text(encoding="utf-8")
    lower = text.lower()
    missing = []
    for category, count in EXPECTED.items():
        pattern = rf"{re.escape(category)}[^\n\r|0-9]{{0,80}}{count}\b|{count}[^\n\r|]{{0,80}}{re.escape(category)}"
        if not re.search(pattern, text, re.IGNORECASE):
            missing.append(f"{category}={count}")
    for section in [
        "executive summary",
        "error counts",
        "component observations",
        "follow-up checks",
    ]:
        if section not in lower:
            missing.append(section)
    for component in ["api", "worker", "scheduler"]:
        if component not in lower:
            missing.append(component)
    if missing:
        print("Summary validation failed: " + ", ".join(missing))
        return 1
    print("Error summary validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
