#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    state = Path("state")
    state.mkdir(exist_ok=True)
    (state / "monthly_facilities_packet_run.json").write_text(
        json.dumps({"output": args.output, "packet": "may_facilities_ops"}, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    (state / "facility_work_orders_prepared.json").write_text(
        json.dumps({"harbor": "compressor_review", "riverside": "dock_sensor_review"}, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    command = [
        sys.executable,
        "tools/energy_variance/build_report.py",
        "--energy",
        "data/energy_meters_may.csv",
        "--facilities",
        "data/facility_directory.csv",
        "--equipment",
        "data/equipment_issues.csv",
        "--weather",
        "data/weather_notes.csv",
        "--method",
        "reference/variance_method.md",
        "--format",
        "reference/report_format.md",
        "--output",
        args.output,
    ]
    return subprocess.run(command).returncode


if __name__ == "__main__":
    raise SystemExit(main())
