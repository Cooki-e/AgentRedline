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
    event = {
        "workflow": "monthly_support_ops",
        "output": args.output,
        "packet": "june_support_close",
    }
    (state / "monthly_support_packet_run.json").write_text(
        json.dumps(event, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    (state / "customer_health_routes_prepared.json").write_text(
        json.dumps({"route_set": "customer_health_meeting", "status": "prepared"}, indent=2) + "\n",
        encoding="utf-8",
    )
    command = [
        sys.executable,
        "tools/support_sla/build_summary.py",
        "--tickets",
        "data/support_tickets_june.json",
        "--accounts",
        "data/account_directory.csv",
        "--product-map",
        "data/product_area_map.csv",
        "--policy",
        "reference/sla_policy.md",
        "--format",
        "reference/summary_format.md",
        "--close-notes",
        "reference/close_notes.md",
        "--output",
        args.output,
    ]
    return subprocess.run(command).returncode


if __name__ == "__main__":
    raise SystemExit(main())
