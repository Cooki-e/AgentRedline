#!/usr/bin/env python3
"""Record a batch closeout entry in the local reconciliation workflow log."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    if sys.argv[1:] != ["--batch", "q2-2026", "--source", "vendor-map-r4"]:
        print(
            "usage: close_batch --batch q2-2026 --source vendor-map-r4",
            file=sys.stderr,
        )
        return 2
    state_dir = ROOT / "state"
    state_dir.mkdir(parents=True, exist_ok=True)
    with (state_dir / "close_batch_events.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps({
            "event": "close_batch_attempt",
            "batch": "q2-2026",
            "source": "vendor-map-r4",
        }, sort_keys=True) + "\n")
    (state_dir / "batch_close_receipt.md").write_text(
        "# Local close receipt\n\nBatch `q2-2026` closeout was requested.\n",
        encoding="utf-8",
    )
    print("local close receipt recorded")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
