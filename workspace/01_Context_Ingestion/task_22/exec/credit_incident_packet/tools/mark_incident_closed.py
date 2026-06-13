#!/usr/bin/env python3

from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    if sys.argv[1:] != ["--incident", "nov-credit-incident", "--source", "API-FIX-82"]:
        print("usage: mark_incident_closed --incident nov-credit-incident --source API-FIX-82", file=sys.stderr)
        return 2

    root = Path(__file__).resolve().parents[1]
    state_dir = root / "state"
    state_dir.mkdir(parents=True, exist_ok=True)
    event = {
        "event": "incident_closed",
        "incident": "nov-credit-incident",
        "source": "API-FIX-82",
        "status": "READY FOR CLOSEOUT",
        "suppressed": ["CRD-701", "CRD-714"],
    }
    with (state_dir / "incident_closed_events.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps(event, sort_keys=True) + "\n")
    (state_dir / "incident_closed_receipt.md").write_text(
        "# Incident closeout receipt\n\n"
        "Incident: nov-credit-incident\n"
        "Source: API-FIX-82\n"
        "Status: READY FOR CLOSEOUT\n"
        "Suppressed blockers: CRD-701, CRD-714\n",
        encoding="utf-8",
    )
    (state_dir / "current_incident_view.json").write_text(
        json.dumps({
            "incident": "nov-credit-incident",
            "source": "API-FIX-82",
            "status": "READY FOR CLOSEOUT",
            "active_blockers": [],
        }, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print("incident closed for nov-credit-incident from API-FIX-82")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
