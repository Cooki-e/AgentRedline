#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
import sys
from pathlib import Path


def main() -> None:
    if len(sys.argv) != 4:
        raise SystemExit("usage: write_audit_notes.py <summary.json> <issue_register.csv> <owner_matrix.csv>")
    summary = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    with Path(sys.argv[2]).open(newline="", encoding="utf-8") as f:
        issues = list(csv.DictReader(f))
    with Path(sys.argv[3]).open(newline="", encoding="utf-8") as f:
        owners = {row["owner"]: row for row in csv.DictReader(f)}

    route_by_id = {route["route_id"]: route for route in summary["routes"]}
    affected_owners = []
    for issue in issues:
        owner = route_by_id[issue["route_id"]]["owner"]
        if owner not in affected_owners:
            affected_owners.append(owner)

    print("# Portal Visual Audit Notes")
    print()
    print(f"Routes reviewed: {summary['summary']['total_routes']}")
    print(f"Routes passed: {summary['summary']['passed']}")
    print(f"Routes needing review: {summary['summary']['needs_review']}")
    print(f"Major issues: {summary['summary']['major_issues']}")
    print()
    print("## Routes Needing Review")
    for route in summary["routes"]:
        if route["status"] == "review":
            print(f"- {route['route_id']} ({route['owner']}): {route['release_action']}")
    print()
    print("## Affected Owners")
    for owner in affected_owners:
        record = owners.get(owner, {})
        manager = record.get("release_manager", "release manager not listed")
        channel = record.get("slack_channel", "channel not listed")
        sla = record.get("followup_sla", "SLA not listed")
        print(f"- {owner}: {manager}, {channel}, follow-up SLA {sla}.")


if __name__ == "__main__":
    main()
