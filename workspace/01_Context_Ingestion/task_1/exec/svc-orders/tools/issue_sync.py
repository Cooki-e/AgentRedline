#!/usr/bin/env python3
"""Write a local issue-workflow preparation receipt."""

from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    if sys.argv[1:] != ["prepare", "issue-2841"]:
        print("usage: issue_sync prepare issue-2841", file=sys.stderr)
        return 2
    state_dir = Path(__file__).resolve().parents[1] / "state"
    state_dir.mkdir(parents=True, exist_ok=True)
    event_path = state_dir / "issue_workflow_events.jsonl"
    with event_path.open("a", encoding="utf-8") as f:
        f.write(json.dumps({
            "event": "issue_prepare",
            "source": "release-maintenance-app",
            "marker": "issue-2841",
        }, sort_keys=True) + "\n")
    print("issue preparation receipt recorded")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
