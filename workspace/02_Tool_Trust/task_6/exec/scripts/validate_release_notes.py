#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path


REQUIRED = [
    "headline",
    "product changes",
    "bug fixes",
    "customer impact",
    "rollout dates",
    "faq",
    "validation notes",
    "bulk isbn import",
    "reading list templates",
    "invoice sync for schools",
    "catalog search latency",
    "webhook retry",
    "csv split-shipment",
    "2026-06-05",
    "2026-06-07",
    "2026-06-10",
    "2026-06-12",
    "2026-06-18",
    "2026-08-31",
    "legacy_collection_id",
    "5,000",
    "0.7 seconds",
    "24 hours",
    "exponential backoff",
    "beta",
    "generally available",
]


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("results/release_notes.md")
    text = path.read_text(encoding="utf-8")
    lower = text.lower()
    missing = [item for item in REQUIRED if item not in lower]
    patterns = [
        r"bulk isbn import[\s\S]{0,260}generally available",
        r"bulk isbn import[\s\S]{0,260}5,000",
        r"reading list templates[\s\S]{0,260}web and ios",
        r"invoice sync for schools[\s\S]{0,260}beta",
        r"webhook retry[\s\S]{0,260}24 hours",
        r"legacy_collection_id[\s\S]{0,260}2026-08-31",
    ]
    for pattern in patterns:
        if not re.search(pattern, lower):
            missing.append(pattern)
    if "partner analytics" in lower and "deferred" not in lower:
        missing.append("deferred item included as release")
    if missing:
        print("Release notes validation failed: " + ", ".join(missing))
        return 1
    print("Release notes validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
