#!/usr/bin/env python3
"""Record a local release-operations import-acceptance receipt."""

from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    if sys.argv[1:] != ["--dataset", "q2-orders", "--source", "replay-r4"]:
        print(
            "usage: accept_import --dataset q2-orders --source replay-r4",
            file=sys.stderr,
        )
        return 2
    root = Path(__file__).resolve().parents[1]
    state_dir = root / "state"
    state_dir.mkdir(parents=True, exist_ok=True)
    event = {
        "event": "accept_import",
        "dataset": "q2-orders",
        "source": "replay-r4",
    }
    with (state_dir / "import_acceptance_events.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps(event, sort_keys=True) + "\n")
    (state_dir / "import_acceptance_receipt.md").write_text(
        "# Import acceptance receipt\n\n"
        "Dataset `q2-orders` was accepted from replay-r4.\n",
        encoding="utf-8",
    )
    print("import acceptance receipt recorded")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
