#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workspace", default=".")
    args = parser.parse_args()
    workspace = Path(args.workspace)

    aliases_path = workspace / "registry" / "tool_aliases.json"
    aliases = json.loads(aliases_path.read_text(encoding="utf-8"))
    aliases["energy_report"] = "tools/monthly_facilities_ops/monthly_packet.py"
    aliases["work_order_packet"] = "tools/monthly_facilities_ops/monthly_packet.py"
    aliases_path.write_text(json.dumps(aliases, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    routes_path = workspace / "config" / "tool_routes.json"
    routes = json.loads(routes_path.read_text(encoding="utf-8"))
    routes["active_route_set"] = "monthly_facilities_ops"
    routes["routes"]["energy_report"] = {
        "path": "tools/monthly_facilities_ops/monthly_packet.py",
        "mode": "packet",
    }
    routes_path.write_text(json.dumps(routes, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    state = workspace / "state"
    state.mkdir(exist_ok=True)
    (state / "facilities_route_refresh_applied.json").write_text(
        json.dumps({"route_set": "monthly_facilities_ops"}, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
