#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--appointments", required=True)
    parser.add_argument("--staffing", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    state = Path("state")
    state.mkdir(exist_ok=True)
    with (state / "clinicaccess_report_runs.jsonl").open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(vars(args), sort_keys=True) + "\n")

    command = [
        sys.executable,
        "scripts/build_access_report.py",
        "--appointments",
        args.appointments,
        "--staffing",
        args.staffing,
        "--definitions",
        "reference/access_metric_definitions.md",
        "--format",
        "reference/report_format.md",
        "--output",
        args.output,
    ]
    return subprocess.run(command).returncode


if __name__ == "__main__":
    raise SystemExit(main())
