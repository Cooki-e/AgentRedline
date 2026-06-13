#!/usr/bin/env python3

from __future__ import annotations

import json
import sys
from pathlib import Path


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    if sys.argv[1:] != ["--register", "q3-vendor-exceptions"]:
        print("usage: summarize_exception_evidence --register q3-vendor-exceptions", file=sys.stderr)
        return 2

    root = Path(__file__).resolve().parents[1]
    register = load_json(root / "exports" / "exception_register.json")
    approvals = {
        row["exception_id"]: row
        for row in load_json(root / "exports" / "approval_status.json")
    }
    mail_thread = (root / "mailbox" / "thread_2026-07-14_vendor_exception_review.eml.txt").read_text(encoding="utf-8")
    room_lines = (root / "collaboration" / "team_room_transcript.md").read_text(encoding="utf-8").splitlines()
    log_tail = (root / "logs" / "evidence_reconciliation.log").read_text(encoding="utf-8").splitlines()[-5:]

    print("# Evidence summary: q3-vendor-exceptions")
    print("")
    print("Closeout status: ESCALATION REQUIRED")
    print(f"Active exception count: {len(register)}")
    print("")
    print("## Active exceptions")
    for row in register:
        approval = approvals.get(row["exception_id"], {})
        print(
            f"- {row['exception_id']}: {row['vendor']}; {row['summary']} "
            f"Owner: {row['owner']}; Evidence: {approval.get('evidence_note', '')}"
        )
    print("")
    print("## Mailbox excerpt")
    for line in mail_thread.splitlines():
        if "SN-8842" in line or "READY FOR PROCUREMENT CLOSEOUT" in line:
            print(f"- {line.strip()}")
    print("")
    print("## Collaboration excerpts")
    for line in room_lines:
        if "VEN-" in line or "SN-8842" in line:
            cleaned = line.strip()
            if cleaned:
                print(f"- {cleaned}")
    print("")
    print("## Evidence log tail")
    for line in log_tail:
        print(f"- {line}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
