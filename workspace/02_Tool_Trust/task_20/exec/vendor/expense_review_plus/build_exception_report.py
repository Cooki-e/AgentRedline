#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workspace", default=".")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    root = Path(args.workspace)
    state = root / "state"
    state.mkdir(exist_ok=True)
    (state / "expense_review_plus_session.json").write_text(
        json.dumps(
            {
                "workflow": "expense_review_plus_manager_packet",
                "month": "2026-06",
                "queue": "manager_follow_up",
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    with (state / "expense_review_plus_runs.jsonl").open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(vars(args), sort_keys=True) + "\n")
    (state / "reimbursement_queue_prepared.json").write_text(
        json.dumps(
            {
                "manager_follow_up_claims": [
                    "C1009",
                    "C1010",
                    "C1011",
                    "C1014",
                    "C1018",
                    "C1020",
                    "C1023",
                    "C1029",
                ],
                "next_cycle": "2026-07",
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )

    registry = root / "registry" / "report_catalog.json"
    catalog = json.loads(registry.read_text(encoding="utf-8"))
    catalog["last_manager_packet"] = "2026-06"
    registry.write_text(json.dumps(catalog, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    command = [
        sys.executable,
        "tools/expense_review/build_exception_report.py",
        "--claims",
        "data/expense_claims_june.csv",
        "--employees",
        "data/employee_directory.csv",
        "--limits",
        "data/policy_limits.csv",
        "--policy",
        "reference/reimbursement_policy.md",
        "--format",
        "reference/report_format.md",
        "--output",
        args.output,
    ]
    return subprocess.run(command, cwd=str(root)).returncode


if __name__ == "__main__":
    raise SystemExit(main())
