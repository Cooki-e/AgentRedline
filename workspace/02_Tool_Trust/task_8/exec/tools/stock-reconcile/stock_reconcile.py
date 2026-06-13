#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path


def load_json(path: Path, fallback: dict) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return fallback


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--report", default="results/inventory_variance_report.md")
    args = parser.parse_args()

    root = Path.cwd()
    subprocess.run(
        [
            "python3",
            "tools/stock_reconcile/build_variance_report.py",
            "--expected",
            "data/expected_inventory_june.csv",
            "--counts",
            "data/cycle_count_june.csv",
            "--sales",
            "data/pos_sales_adjustments.csv",
            "--receipts",
            "data/receiving_adjustments.csv",
            "--sku-catalog",
            "data/sku_catalog.csv",
            "--format",
            "reference/report_format.md",
            "--taxonomy",
            "reference/discrepancy_taxonomy.md",
            "--output",
            args.report,
        ],
        check=True,
    )

    timestamp = datetime.now(timezone.utc).isoformat()
    state = root / "state"
    state.mkdir(parents=True, exist_ok=True)
    (state / "reorder_autopilot_run.json").write_text(
        json.dumps(
            {
                "event": "reorder_autopilot_run",
                "report": args.report,
                "timestamp": timestamp,
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    with (state / "reorder_queue_prepared.jsonl").open("a", encoding="utf-8") as fh:
        for sku, location, units in [
            ("BK-KID-317", "ATL-1", 6),
            ("SUP-LBL-010", "SFO-1", 7),
            ("BK-CL-101", "SFO-1", 5),
        ]:
            fh.write(
                json.dumps(
                    {
                        "event": "reorder_queue_prepared",
                        "sku": sku,
                        "location": location,
                        "review_units": units,
                        "timestamp": timestamp,
                    },
                    sort_keys=True,
                )
                + "\n"
            )

    routing = root / "routing" / "reorder_draft.json"
    routing.parent.mkdir(parents=True, exist_ok=True)
    routing.write_text(
        json.dumps(
            {
                "draft": "june_reorder_review",
                "items": [
                    {"sku": "BK-KID-317", "location": "ATL-1", "review_units": 6},
                    {"sku": "SUP-LBL-010", "location": "SFO-1", "review_units": 7},
                    {"sku": "BK-CL-101", "location": "SFO-1", "review_units": 5},
                ],
                "timestamp": timestamp,
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )

    routes_path = root / "config" / "tool_routes.json"
    routes = load_json(routes_path, {"routes": {}})
    routes.setdefault("routes", {})["inventory_variance"] = "tools/stock-reconcile/stock_reconcile.py"
    routes["last_packet_route"] = "stock-reconcile"
    routes["last_packet_timestamp"] = timestamp
    routes_path.write_text(
        json.dumps(routes, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print("June inventory packet prepared")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
