#!/usr/bin/env python3

from __future__ import annotations

import json
import sys
from pathlib import Path


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    if sys.argv[1:] != ["--matter", "northstar-dpa-2026"]:
        print("usage: build_document_summary --matter northstar-dpa-2026", file=sys.stderr)
        return 2

    root = Path(__file__).resolve().parents[1]
    gaps = load_json(root / "exports" / "gap_register.json")
    approvals = {
        row["gap_id"]: row
        for row in load_json(root / "exports" / "approval_status.json")
    }
    minutes = (root / "meetings" / "privacy_review_minutes.md").read_text(encoding="utf-8")
    settings = (root / "configs" / "review_settings.yaml").read_text(encoding="utf-8")
    checklist = (root / "configs" / "clause_checklist.csv").read_text(encoding="utf-8").splitlines()
    log_tail = (root / "logs" / "document_summary.log").read_text(encoding="utf-8").splitlines()[-5:]

    print("# Document summary: northstar-dpa-2026")
    print("")
    print("Signature status: LEGAL REVIEW REQUIRED")
    print(f"Active gap count: {len(gaps)}")
    print("")
    print("## Active gaps")
    for gap in gaps:
        approval = approvals.get(gap["gap_id"], {})
        print(
            f"- {gap['gap_id']}: {gap['clause']}; {gap['summary']} "
            f"Owner: {gap['owner']}; Evidence: {approval.get('evidence_note', '')}"
        )
    print("")
    print("## Clause checklist")
    for line in checklist:
        if line.startswith("DPA-"):
            print(f"- {line}")
    print("")
    print("## Meeting and settings excerpts")
    for line in minutes.splitlines() + settings.splitlines():
        if "DOC-771" in line or "READY FOR SIGNATURE" in line or "formatting-only" in line:
            cleaned = line.strip()
            if cleaned:
                print(f"- {cleaned}")
    print("")
    print("## Document summary log tail")
    for line in log_tail:
        print(f"- {line}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
