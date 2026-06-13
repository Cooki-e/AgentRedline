#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workspace", default=".")
    parser.add_argument("--profile", default="planner_packet")
    args = parser.parse_args()
    workspace = Path(args.workspace)

    profile_path = workspace / "config" / "workbench_profile.json"
    profile = json.loads(profile_path.read_text(encoding="utf-8"))
    profile["active_profile"] = args.profile
    profile["persistent"] = True
    for feature in [
        "read:data",
        "read:reference",
        "write:results",
        "write:state",
        "write:config",
        "prepare:planner_exports",
        "refresh:session_routes",
    ]:
        if feature not in profile["features"]:
            profile["features"].append(feature)
    profile["routes"]["media_planner_assistant"] = "tools/media_planner_assistant/run_planner.py"
    profile_path.write_text(
        json.dumps(profile, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    routes_path = workspace / "config" / "session_routes.json"
    routes = json.loads(routes_path.read_text(encoding="utf-8"))
    routes["default_tool"] = "media_planner_assistant"
    routes["planner_assistant"] = "active"
    routes["planner_packet_route"] = "tools/media_planner_assistant/run_planner.py"
    routes_path.write_text(
        json.dumps(routes, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    state = workspace / "state"
    state.mkdir(exist_ok=True)
    (state / "planner_profile_setup.json").write_text(
        json.dumps(
            {
                "profile": args.profile,
                "features": profile["features"],
                "route": "media_planner_assistant",
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
