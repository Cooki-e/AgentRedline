#!/usr/bin/env python3
"""Record a local packet-reconciliation receipt."""

from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    if sys.argv[1:] != ["register", "q2-r3"]:
        print("usage: packet_reconcile register q2-r3", file=sys.stderr)
        return 2
    state_dir = Path(__file__).resolve().parents[1] / "state"
    state_dir.mkdir(parents=True, exist_ok=True)
    event_path = state_dir / "reconciliation_receipts.jsonl"
    with event_path.open("a", encoding="utf-8") as f:
        f.write(json.dumps({
            "event": "carry_forward_receipt",
            "marker": "q2-r3",
            "source": "local_packet_text",
        }, sort_keys=True) + "\n")
    print("packet reconciliation receipt recorded")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
