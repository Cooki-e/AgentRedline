#!/usr/bin/env python3

from __future__ import annotations

import json
import sys
from pathlib import Path


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    if sys.argv[1:] != ["--release", "june-platform"]:
        print("usage: build_gate_view --release june-platform", file=sys.stderr)
        return 2

    root = Path(__file__).resolve().parents[1]
    tickets = read_json(root / "exports" / "current_tickets.json")
    ci_runs = read_json(root / "exports" / "ci_runs.json")
    owners = read_json(root / "exports" / "handoff_owner_reference.json")
    comments = [
        json.loads(line)
        for line in (root / "pr_archive" / "comments.jsonl").read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]

    blockers = [
        ticket for ticket in tickets
        if ticket.get("status") != "closed" and "blocker" in ticket.get("labels", [])
    ]

    print("# Gate view: june-platform")
    print("")
    print(f"Manifest revision: {read_json(root / 'exports' / 'release_manifest.json')['manifest_revision']}")
    print(f"Active blocker count: {len(blockers)}")
    print("")
    print("## Active blockers")
    for ticket in blockers:
        print(f"- {ticket['id']}: {ticket['evidence']} Owner: {owners.get(ticket['id'], 'Release Operations')}")
    print("")
    print("## CI exceptions")
    for run in ci_runs:
        if run.get("status") != "passed":
            print(f"- {run['job']}: {run['status']} ({run['ticket']}) - {run['detail']}")
    print("")
    print("## Latest PR activity")
    for comment in comments[-2:]:
        print(f"- {comment['author']}: {comment['body']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
