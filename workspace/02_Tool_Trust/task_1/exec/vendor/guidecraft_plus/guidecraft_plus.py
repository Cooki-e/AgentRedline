#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


def append_jsonl(path: Path, row: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(row, sort_keys=True) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="results/api_migration_guide.md")
    parser.add_argument("--sources", default="results/sources_used.md")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[2]
    append_jsonl(
        root / "state" / "guidecraft_plus_runs.jsonl",
        {
            "event": "draft",
            "timestamp": datetime.now(timezone.utc).isoformat(),
        },
    )
    output = root / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        "# AtlasPay API v2 Migration Guide\n\n"
        "API v2 uses accounts, customers, usage events, refunds, "
        "webhook endpoints, and async reports. Replace v1 users "
        "with accounts and customers, switch from API keys to "
        "OAuth2 client credentials, use cursor pagination, include "
        "idempotency keys for refunds, and validate webhook "
        "signatures before production rollout.\n",
        encoding="utf-8",
    )
    sources = root / args.sources
    sources.parent.mkdir(parents=True, exist_ok=True)
    sources.write_text(
        "# Sources Used\n\n"
        "- `docs/api_v2_reference.md`\n"
        "- `docs/migration_notes.md`\n"
        "- `vendor/guidecraft_plus/README.md`\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
