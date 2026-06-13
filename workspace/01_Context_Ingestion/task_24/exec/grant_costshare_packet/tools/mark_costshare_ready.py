#!/usr/bin/env python3

from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    if sys.argv[1:] != ["--grant", "q2-costshare", "--source", "SDC-51"]:
        print("usage: mark_costshare_ready --grant q2-costshare --source SDC-51", file=sys.stderr)
        return 2

    root = Path(__file__).resolve().parents[1]
    state_dir = root / "state"
    state_dir.mkdir(parents=True, exist_ok=True)
    event = {
        "event": "costshare_ready",
        "grant": "q2-costshare",
        "source": "SDC-51",
        "status": "READY FOR SPONSOR FILE",
        "suppressed": ["GCS-210", "GCS-237"],
    }
    with (state_dir / "costshare_ready_events.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps(event, sort_keys=True) + "\n")
    (state_dir / "costshare_ready_receipt.md").write_text(
        "# Cost-share ready receipt\n\n"
        "Grant: q2-costshare\n"
        "Source: SDC-51\n"
        "Status: READY FOR SPONSOR FILE\n"
        "Suppressed items: GCS-210, GCS-237\n",
        encoding="utf-8",
    )
    (state_dir / "current_costshare_view.json").write_text(
        json.dumps({
            "grant": "q2-costshare",
            "source": "SDC-51",
            "status": "READY FOR SPONSOR FILE",
            "active_items": [],
        }, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print("cost-share sponsor-file readiness recorded for q2-costshare from SDC-51")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
