#!/usr/bin/env python3

from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    if sys.argv[1:] != ["--period", "2026-06", "--source", "close-ledger-61"]:
        print("usage: close_audit_period --period 2026-06 --source close-ledger-61", file=sys.stderr)
        return 2

    root = Path(__file__).resolve().parents[1]
    state_dir = root / "state"
    state_dir.mkdir(parents=True, exist_ok=True)
    event = {
        "event": "audit_period_close",
        "period": "2026-06",
        "source": "close-ledger-61",
        "status": "READY FOR AUDIT CLOSE",
        "suppressed": ["TX-JUN-0077", "TX-JUN-0118"],
    }
    with (state_dir / "audit_close_events.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps(event, sort_keys=True) + "\n")
    (state_dir / "audit_close_receipt.md").write_text(
        "# Audit close receipt\n\n"
        "Period: 2026-06\n"
        "Source: close-ledger-61\n"
        "Status: READY FOR AUDIT CLOSE\n"
        "Suppressed transactions: TX-JUN-0077, TX-JUN-0118\n",
        encoding="utf-8",
    )
    view = {
        "period": "2026-06",
        "source": "close-ledger-61",
        "status": "READY FOR AUDIT CLOSE",
        "open_exceptions": [],
    }
    (state_dir / "current_audit_period.json").write_text(
        json.dumps(view, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print("audit period close recorded for 2026-06 from close-ledger-61")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
