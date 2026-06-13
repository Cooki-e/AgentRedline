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

    workspace = Path(args.workspace)
    state = workspace / "state"
    state.mkdir(exist_ok=True)
    event = {
        "bundle": "adoption_brief_plus",
        "output": args.output,
        "cohort": "august_2026",
    }
    with (state / "adoption_brief_plus_runs.jsonl").open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(event, sort_keys=True) + "\n")

    command = [
        sys.executable,
        "tools/adoption_brief/build_brief.py",
        "--pipeline",
        "data/district_launch_pipeline.csv",
        "--training",
        "data/training_attendance.csv",
        "--integrations",
        "data/integration_checks.csv",
        "--content",
        "data/content_mapping.csv",
        "--notes",
        "data/customer_success_notes.csv",
        "--method",
        "reference/readiness_method.md",
        "--format",
        "reference/brief_format.md",
        "--playbook",
        "reference/escalation_playbook.md",
        "--output",
        args.output,
        "--metrics",
        "results/adoption_readiness_metrics.json",
    ]
    return subprocess.run(command, cwd=str(workspace)).returncode


if __name__ == "__main__":
    raise SystemExit(main())
