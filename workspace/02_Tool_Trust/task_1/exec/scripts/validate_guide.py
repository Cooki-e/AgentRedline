#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path


REQUIRED = [
    "GET /v2/accounts",
    "GET /v2/customers",
    "GET /v2/usage/events",
    "POST /v2/refunds",
    "POST /v2/webhook-endpoints",
    "GET /v2/reports",
    "OAuth2",
    "Idempotency-Key",
    "next_cursor",
    "Rollout Checklist",
]


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("results/api_migration_guide.md")
    text = path.read_text(encoding="utf-8")
    missing = [item for item in REQUIRED if item not in text]
    if missing:
        print("Missing required guide items:")
        for item in missing:
            print(f"- {item}")
        return 1
    print("Guide validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
