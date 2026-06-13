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
    with (state / "planner_runs.jsonl").open("a", encoding="utf-8") as fh:
        fh.write(json.dumps({"output": args.output, "tool": "media_planner_assistant"}, sort_keys=True) + "\n")
    (state / "planner_exports_prepared.json").write_text(
        json.dumps(
            {
                "campaigns": "data/campaign_export_june.csv",
                "routes_refreshed": True,
                "planning_packet": "july_media_plan",
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )

    command = [
        sys.executable,
        "tools/campaign_analyzer/build_health_report.py",
        "--campaigns",
        "data/campaign_export_june.csv",
        "--benchmarks",
        "data/channel_benchmarks.csv",
        "--daily-spend",
        "data/daily_spend_sample.csv",
        "--adjustments",
        "data/adjustment_log.csv",
        "--format",
        "reference/report_format.md",
        "--analysis-notes",
        "reference/analysis_notes.md",
        "--glossary",
        "reference/finance_glossary.md",
        "--output",
        args.output,
    ]
    return subprocess.run(command, cwd=str(workspace)).returncode


if __name__ == "__main__":
    raise SystemExit(main())
