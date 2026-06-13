#!/usr/bin/env python3
from __future__ import annotations

import argparse
import subprocess


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="results/q3_forecast_summary.md")
    args = parser.parse_args()

    steps = [
        [
            "python3",
            "mcp_servers/forecast_plus/register_server.py",
            "--profile",
            "config/mcp_servers.json",
            "--session-tools",
            "config/session_tools.json",
            "--enable-autostart",
        ],
        [
            "python3",
            "tools/forecast_calc/calc_forecast.py",
            "--pipeline",
            "data/pipeline_q3_2026.csv",
            "--win-rates",
            "data/historical_win_rates.csv",
            "--segments",
            "data/account_segments.csv",
            "--format-guide",
            "reference/summary_format.md",
            "--risk-taxonomy",
            "reference/risk_taxonomy.md",
            "--output",
            args.output,
        ],
        [
            "python3",
            "scripts/validate_forecast_summary.py",
            args.output,
        ],
    ]
    for step in steps:
        subprocess.run(step, check=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
