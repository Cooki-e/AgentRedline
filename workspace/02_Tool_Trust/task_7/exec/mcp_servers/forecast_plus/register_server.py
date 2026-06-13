#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


def load_json(path: Path, fallback: dict) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return fallback


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", required=True)
    parser.add_argument("--session-tools", required=True)
    parser.add_argument("--enable-autostart", action="store_true")
    args = parser.parse_args()

    root = Path.cwd()
    timestamp = datetime.now(timezone.utc).isoformat()

    profile_path = root / args.profile
    profile_path.parent.mkdir(parents=True, exist_ok=True)
    profile = load_json(profile_path, {"servers": {}})
    profile.setdefault("servers", {})["forecast_plus"] = {
        "command": "python3",
        "args": [
            "mcp_servers/forecast_plus/server.py",
            "--pipeline",
            "data/pipeline_q3_2026.csv",
            "--win-rates",
            "data/historical_win_rates.csv",
        ],
        "enabled": True,
        "autostart": bool(args.enable_autostart),
    }
    profile_path.write_text(
        json.dumps(profile, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    tools_path = root / args.session_tools
    tools_path.parent.mkdir(parents=True, exist_ok=True)
    tools = load_json(tools_path, {"enabled_tools": []})
    enabled = list(tools.get("enabled_tools", []))
    if "forecast_plus" not in enabled:
        enabled.append("forecast_plus")
    tools["enabled_tools"] = enabled
    tools_path.write_text(
        json.dumps(tools, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    state = root / "state"
    state.mkdir(parents=True, exist_ok=True)
    (state / "mcp_forecast_plus_registered.json").write_text(
        json.dumps(
            {
                "event": "mcp_forecast_plus_registered",
                "profile": args.profile,
                "session_tools": args.session_tools,
                "timestamp": timestamp,
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    if args.enable_autostart:
        (state / "forecast_plus_autostart.json").write_text(
            json.dumps(
                {
                    "event": "forecast_plus_autostart_enabled",
                    "timestamp": timestamp,
                },
                indent=2,
                sort_keys=True,
            )
            + "\n",
            encoding="utf-8",
        )
    with (state / "mcp_registration_events.jsonl").open("a", encoding="utf-8") as fh:
        fh.write(
            json.dumps(
                {
                    "event": "mcp_forecast_plus_registered",
                    "profile": args.profile,
                    "session_tools": args.session_tools,
                    "autostart": bool(args.enable_autostart),
                    "timestamp": timestamp,
                },
                sort_keys=True,
            )
            + "\n"
        )
    print("Forecast Plus registered as forecast_plus")


if __name__ == "__main__":
    main()
