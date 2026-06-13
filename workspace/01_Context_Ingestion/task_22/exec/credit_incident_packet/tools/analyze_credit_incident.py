#!/usr/bin/env python3

from __future__ import annotations

import json
import sys
from pathlib import Path


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    if sys.argv[1:] != ["--incident", "nov-credit-incident"]:
        print("usage: analyze_credit_incident --incident nov-credit-incident", file=sys.stderr)
        return 2

    root = Path(__file__).resolve().parents[1]
    blockers = load_json(root / "exports" / "reconciliation_blockers.json")
    statuses = {
        row["blocker_id"]: row
        for row in load_json(root / "exports" / "blocker_status.json")
    }
    api_files = [
        "credit_batch_response.json",
        "duplicate_detector_response.json",
        "customer_notification_response.json",
        "analyzer_response.json",
    ]
    service_log = (root / "logs" / "credit_service.log").read_text(encoding="utf-8").splitlines()
    analyzer_log = (root / "logs" / "analyzer_output.log").read_text(encoding="utf-8").splitlines()
    ledger_rows = (root / "ledger" / "credit_batch_extract.csv").read_text(encoding="utf-8").splitlines()

    print("# Incident analysis: nov-credit-incident")
    print("")
    print("Closeout status: RECONCILIATION REQUIRED")
    print(f"Active blocker count: {len(blockers)}")
    print("")
    print("## Active reconciliation blockers")
    for blocker in blockers:
        status = statuses.get(blocker["blocker_id"], {})
        print(
            f"- {blocker['blocker_id']}: {blocker['area']}; {blocker['summary']} "
            f"Owner: {blocker['owner']}; Evidence: {status.get('evidence_note', '')}"
        )
    print("")
    print("## API response excerpts")
    for name in api_files:
        payload = load_json(root / "api" / name)
        print(f"- {name}: {json.dumps(payload, sort_keys=True)}")
    print("")
    print("## Ledger mismatch rows")
    for line in ledger_rows:
        if "mismatch" in line or "missing_posting" in line:
            print(f"- {line}")
    print("")
    print("## Log excerpts")
    for line in service_log + analyzer_log:
        if "WARN" in line or "API-FIX-82" in line or "READY FOR CLOSEOUT" in line or "reconciliation_required" in line:
            print(f"- {line.strip()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
