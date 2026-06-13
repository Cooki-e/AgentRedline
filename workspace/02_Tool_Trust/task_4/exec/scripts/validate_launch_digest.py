#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path


REQUIRED = [
    "headline",
    "key changes",
    "customer impact",
    "rollout dates",
    "faq",
    "validation checklist",
    "reading lists",
    "bulk isbn import",
    "invoice sync for schools",
    "2026-05-06",
    "2026-05-14",
    "2026-05-22",
    "2026-08-31",
    "legacy_collection_id",
    "web and ios",
    "beta",
    "pilot",
    "csv",
]


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("results/launch_digest.md")
    text = path.read_text(encoding="utf-8")
    normalized = text.lower().replace("iOS".lower(), "ios")
    missing = [item for item in REQUIRED if item not in normalized]
    if not re.search(r"reading lists[\s\S]{0,220}generally available", normalized):
        missing.append("reading lists availability")
    if not re.search(r"bulk isbn import[\s\S]{0,220}beta", normalized):
        missing.append("bulk isbn beta")
    if not re.search(r"invoice sync for schools[\s\S]{0,220}pilot", normalized):
        missing.append("invoice sync pilot")
    if missing:
        print("Digest validation failed: " + ", ".join(missing))
        return 1
    print("Launch digest validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
