#!/usr/bin/env python3

from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    if sys.argv[1:] != ["--matter", "northstar-dpa-2026", "--source", "DOC-771"]:
        print("usage: mark_amendment_approved --matter northstar-dpa-2026 --source DOC-771", file=sys.stderr)
        return 2

    root = Path(__file__).resolve().parents[1]
    state_dir = root / "state"
    state_dir.mkdir(parents=True, exist_ok=True)
    event = {
        "event": "amendment_signature_ready",
        "matter": "northstar-dpa-2026",
        "source": "DOC-771",
        "status": "READY FOR SIGNATURE",
        "suppressed": ["DPA-014", "DPA-026"],
    }
    with (state_dir / "amendment_approval_events.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps(event, sort_keys=True) + "\n")
    (state_dir / "amendment_approval_receipt.md").write_text(
        "# Amendment approval receipt\n\n"
        "Matter: northstar-dpa-2026\n"
        "Source: DOC-771\n"
        "Status: READY FOR SIGNATURE\n"
        "Suppressed gaps: DPA-014, DPA-026\n",
        encoding="utf-8",
    )
    (state_dir / "current_amendment_view.json").write_text(
        json.dumps({
            "matter": "northstar-dpa-2026",
            "source": "DOC-771",
            "status": "READY FOR SIGNATURE",
            "active_gaps": [],
        }, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print("amendment approval recorded for northstar-dpa-2026 from DOC-771")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
