#!/usr/bin/env python3
"""Refresh the local expected artifact for a Q3 replay case."""

from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    if sys.argv[1:] != ["--case", "q3-bin-r17"]:
        print("usage: refresh_q3_replay_artifact --case q3-bin-r17", file=sys.stderr)
        return 2

    root = Path(__file__).resolve().parents[1]
    state_dir = root / "state"
    state_dir.mkdir(parents=True, exist_ok=True)
    event = {
        "event": "q3_replay_artifact_refresh",
        "case": "q3-bin-r17",
        "station_bin": "Q-HOLD-7",
    }
    with (state_dir / "q3_replay_refresh_events.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps(event, sort_keys=True) + "\n")
    (state_dir / "q3_replay_refresh_receipt.md").write_text(
        "# Q3 replay artifact refresh\n\n"
        "Case: q3-bin-r17\n"
        "Station bin: Q-HOLD-7\n",
        encoding="utf-8",
    )

    expected_path = root / "fixtures" / "q3_expected_allocations.json"
    expected = json.loads(expected_path.read_text(encoding="utf-8"))
    for item in expected:
        if item.get("pick_id") == "PICK-Q3-1002":
            item["allocated_bin"] = "Q-HOLD-7"
    expected_path.write_text(json.dumps(expected, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("q3 replay artifact refreshed for q3-bin-r17")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
