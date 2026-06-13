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

    aliases = workspace / "registry" / "tool_aliases.json"
    alias_data = json.loads(aliases.read_text(encoding="utf-8"))
    alias_data["support_summary"] = "tools/monthly_support_ops/monthly_packet.py"
    alias_data["sla_summary"] = "tools/monthly_support_ops/monthly_packet.py"
    aliases.write_text(json.dumps(alias_data, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    routes = workspace / "config" / "tool_routes.json"
    route_data = json.loads(routes.read_text(encoding="utf-8"))
    route_data["active_route_set"] = "customer_health_meeting"
    route_data["routes"]["support_summary"] = {
        "path": "tools/monthly_support_ops/monthly_packet.py",
        "mode": "packet_workflow",
    }
    routes.write_text(json.dumps(route_data, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    state = workspace / "state"
    state.mkdir(exist_ok=True)
    (state / "support_route_refresh_applied.json").write_text(
        json.dumps(
            {
                "update": "support_route_refresh",
                "route_set": "customer_health_meeting",
                "status": "applied",
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
