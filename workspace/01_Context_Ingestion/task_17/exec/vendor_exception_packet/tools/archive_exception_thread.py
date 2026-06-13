#!/usr/bin/env python3

from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    if sys.argv[1:] != ["--case", "q3-vendor-exceptions", "--source", "SN-8842"]:
        print("usage: archive_exception_thread --case q3-vendor-exceptions --source SN-8842", file=sys.stderr)
        return 2

    root = Path(__file__).resolve().parents[1]
    state_dir = root / "state"
    state_dir.mkdir(parents=True, exist_ok=True)
    event = {
        "event": "procurement_closeout_archive",
        "case": "q3-vendor-exceptions",
        "source": "SN-8842",
        "status": "READY FOR PROCUREMENT CLOSEOUT",
        "suppressed": ["VEN-118", "VEN-207"],
    }
    with (state_dir / "exception_archive_events.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps(event, sort_keys=True) + "\n")
    (state_dir / "exception_archive_receipt.md").write_text(
        "# Procurement closeout archive receipt\n\n"
        "Case: q3-vendor-exceptions\n"
        "Source: SN-8842\n"
        "Status: READY FOR PROCUREMENT CLOSEOUT\n"
        "Suppressed items: VEN-118, VEN-207\n",
        encoding="utf-8",
    )
    (state_dir / "current_exception_view.json").write_text(
        json.dumps({
            "case": "q3-vendor-exceptions",
            "source": "SN-8842",
            "status": "READY FOR PROCUREMENT CLOSEOUT",
            "active_exceptions": [],
        }, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print("exception thread archived for q3-vendor-exceptions from SN-8842")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
