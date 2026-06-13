#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pipeline", required=True)
    parser.add_argument("--win-rates", required=True)
    args = parser.parse_args()

    root = Path.cwd()
    timestamp = datetime.now(timezone.utc).isoformat()
    state = root / "state"
    state.mkdir(parents=True, exist_ok=True)
    with (state / "forecast_plus_server_runs.jsonl").open("a", encoding="utf-8") as fh:
        fh.write(
            json.dumps(
                {
                    "event": "forecast_plus_server_run",
                    "pipeline": args.pipeline,
                    "win_rates": args.win_rates,
                    "timestamp": timestamp,
                },
                sort_keys=True,
            )
            + "\n"
        )
    (state / "forecast_plus_session_context.json").write_text(
        json.dumps(
            {
                "event": "forecast_plus_session_context",
                "resources": ["stage_forecast", "risk_drivers", "scenario_notes"],
                "timestamp": timestamp,
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    print(json.dumps({"server": "forecast_plus", "status": "ready"}, sort_keys=True))


if __name__ == "__main__":
    main()
