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
    parser.add_argument("--refresh-layout", action="store_true")
    args = parser.parse_args()

    workspace = Path(args.workspace)
    state_dir = workspace / "state"
    state_dir.mkdir(exist_ok=True)
    session = {
        "package": "ap_aging_pro",
        "version": "2.8.0",
        "workspace": str(workspace),
        "output": args.output,
        "layout": "controller_review",
    }
    (state_dir / "ap_aging_pro_session.json").write_text(
        json.dumps(session, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    (state_dir / "ap_aging_pro_runs.jsonl").open("a", encoding="utf-8").write(
        json.dumps(session, sort_keys=True) + "\n"
    )

    command = [
        sys.executable,
        "tools/ap_aging/export_aging.py",
        "--payables",
        "data/payables_june.csv",
        "--vendors",
        "data/vendor_directory.csv",
        "--terms",
        "data/payment_terms.csv",
        "--method",
        "reference/aging_method.md",
        "--format",
        "reference/report_format.md",
        "--output",
        args.output,
        "--metrics",
        "results/payables_aging_metrics.json",
    ]
    return subprocess.run(command, cwd=str(workspace)).returncode


if __name__ == "__main__":
    raise SystemExit(main())
