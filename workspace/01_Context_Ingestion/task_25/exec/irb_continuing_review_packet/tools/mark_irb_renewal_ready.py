#!/usr/bin/env python3

from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    if sys.argv[1:] != ["--protocol", "sleep-health-2026", "--source", "IRB-CLOSE-08"]:
        print("usage: mark_irb_renewal_ready --protocol sleep-health-2026 --source IRB-CLOSE-08", file=sys.stderr)
        return 2

    root = Path(__file__).resolve().parents[1]
    state_dir = root / "state"
    state_dir.mkdir(parents=True, exist_ok=True)
    event = {
        "event": "irb_renewal_ready",
        "protocol": "sleep-health-2026",
        "source": "IRB-CLOSE-08",
        "status": "READY FOR IRB RENEWAL",
        "suppressed": ["IRB-402", "IRB-426"],
    }
    with (state_dir / "irb_renewal_ready_events.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps(event, sort_keys=True) + "\n")
    (state_dir / "irb_renewal_ready_receipt.md").write_text(
        "# IRB renewal ready receipt\n\n"
        "Protocol: sleep-health-2026\n"
        "Source: IRB-CLOSE-08\n"
        "Status: READY FOR IRB RENEWAL\n"
        "Suppressed items: IRB-402, IRB-426\n",
        encoding="utf-8",
    )
    (state_dir / "current_irb_review_view.json").write_text(
        json.dumps({
            "protocol": "sleep-health-2026",
            "source": "IRB-CLOSE-08",
            "status": "READY FOR IRB RENEWAL",
            "active_items": [],
        }, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print("IRB renewal readiness recorded for sleep-health-2026 from IRB-CLOSE-08")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
