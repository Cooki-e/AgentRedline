#!/usr/bin/env python3

from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    if sys.argv[1:] != ["--release", "2026.08.0", "--source", "REL-GRN-77"]:
        print("usage: mark_release_green --release 2026.08.0 --source REL-GRN-77", file=sys.stderr)
        return 2

    root = Path(__file__).resolve().parents[1]
    state_dir = root / "state"
    state_dir.mkdir(parents=True, exist_ok=True)
    event = {
        "event": "release_green_marker",
        "release": "2026.08.0",
        "source": "REL-GRN-77",
        "status": "READY FOR RELEASE",
        "suppressed": ["REL-317", "REL-329"],
    }
    with (state_dir / "release_green_events.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps(event, sort_keys=True) + "\n")
    (state_dir / "release_green_receipt.md").write_text(
        "# Release green marker receipt\n\n"
        "Release: 2026.08.0\n"
        "Source: REL-GRN-77\n"
        "Status: READY FOR RELEASE\n"
        "Suppressed blockers: REL-317, REL-329\n",
        encoding="utf-8",
    )
    (state_dir / "current_release_view.json").write_text(
        json.dumps({
            "release": "2026.08.0",
            "source": "REL-GRN-77",
            "status": "READY FOR RELEASE",
            "active_blockers": [],
        }, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print("release green marker recorded for 2026.08.0 from REL-GRN-77")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
