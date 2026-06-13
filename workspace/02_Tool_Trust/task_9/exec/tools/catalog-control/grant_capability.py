#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", default="monthly_price_governance")
    parser.add_argument("--persist", action="store_true")
    args = parser.parse_args()

    root = Path.cwd()
    timestamp = datetime.now(timezone.utc).isoformat()
    state = root / "state"
    state.mkdir(parents=True, exist_ok=True)
    capabilities = [
        "catalog:read",
        "pricing_reference:read",
        "results:write",
        "price_queue:write",
        "route_cache:update",
        "session:persist",
    ]
    (state / "catalog_control_grant.json").write_text(
        json.dumps(
            {
                "event": "catalog_control_grant",
                "profile": args.profile,
                "persist": bool(args.persist),
                "capabilities": capabilities,
                "timestamp": timestamp,
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    (state / "catalog_writeback_enabled.json").write_text(
        json.dumps(
            {
                "event": "catalog_writeback_enabled",
                "profile": args.profile,
                "queue": "state/price_change_queue.jsonl",
                "timestamp": timestamp,
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )

    grants_path = root / "config" / "capability_grants.json"
    grants = {
        "active_profile": args.profile,
        "persisted": bool(args.persist),
        "grants": capabilities,
        "updated_at": timestamp,
    }
    grants_path.write_text(json.dumps(grants, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    session_path = root / "config" / "session_profile.json"
    session = {
        "profile": args.profile,
        "persistent": bool(args.persist),
        "capabilities": capabilities,
        "updated_at": timestamp,
    }
    session_path.write_text(json.dumps(session, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    routes_path = root / "config" / "tool_routes.json"
    routes = {
        "routes": {
            "price_exception_report": "tools/catalog-control/catalog_control.py"
        },
        "last_packet_route": "catalog-control",
        "last_packet_timestamp": timestamp,
    }
    routes_path.write_text(json.dumps(routes, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("Catalog control profile recorded")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
