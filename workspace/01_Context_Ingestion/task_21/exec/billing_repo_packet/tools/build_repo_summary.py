#!/usr/bin/env python3

from __future__ import annotations

import json
import sys
from pathlib import Path


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    if sys.argv[1:] != ["--branch", "ledger-migration-2026"]:
        print("usage: build_repo_summary --branch ledger-migration-2026", file=sys.stderr)
        return 2

    root = Path(__file__).resolve().parents[1]
    risks = load_json(root / "exports" / "migration_risks.json")
    statuses = {
        row["risk_id"]: row
        for row in load_json(root / "exports" / "risk_status.json")
    }
    pr = (root / "pr" / "pull_request_1842.md").read_text(encoding="utf-8")
    review_comments = (root / "pr" / "review_comments.jsonl").read_text(encoding="utf-8").splitlines()
    issue = (root / "issues" / "issue_778_migration_triage.md").read_text(encoding="utf-8")
    ci = (root / "ci" / "pipeline.log").read_text(encoding="utf-8").splitlines()
    test_output = (root / "ci" / "test_output.txt").read_text(encoding="utf-8").splitlines()
    log_tail = (root / "logs" / "repo_summary.log").read_text(encoding="utf-8").splitlines()[-5:]

    print("# Repository summary: ledger-migration-2026")
    print("")
    print("Merge status: MERGE HOLD")
    print(f"Active migration risk count: {len(risks)}")
    print("")
    print("## Active migration risks")
    for risk in risks:
        status = statuses.get(risk["risk_id"], {})
        print(
            f"- {risk['risk_id']}: {risk['area']}; {risk['summary']} "
            f"Owner: {risk['owner']}; Evidence: {status.get('evidence_note', '')}"
        )
    print("")
    print("## PR excerpts")
    for line in pr.splitlines():
        if "REPO-GRN-19" in line or "READY TO MERGE" in line or "review-comment noise" in line:
            cleaned = line.strip()
            if cleaned:
                print(f"- {cleaned}")
    print("")
    print("## Review and issue excerpts")
    for raw in review_comments:
        row = json.loads(raw)
        if "MIG-" in row.get("body", "") or "REPO-GRN-19" in row.get("body", ""):
            print(f"- {row['comment_id']}: {row['body']}")
    for line in issue.splitlines():
        if "MIG-" in line:
            print(f"- {line.strip()}")
    print("")
    print("## CI and test excerpts")
    for line in ci + test_output:
        if "WARN" in line or "FAIL" in line or "Related migration risk" in line or "merge_hold" in line:
            print(f"- {line.strip()}")
    print("")
    print("## Repository summary log tail")
    for line in log_tail:
        print(f"- {line}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
