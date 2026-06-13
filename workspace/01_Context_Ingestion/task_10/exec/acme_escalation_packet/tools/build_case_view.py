#!/usr/bin/env python3

from __future__ import annotations

import json
import sys
from pathlib import Path


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def read_jsonl(path: Path):
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def main() -> int:
    if sys.argv[1:] != ["--account", "acme-corp"]:
        print("usage: build_case_view --account acme-corp", file=sys.stderr)
        return 2

    root = Path(__file__).resolve().parents[1]
    profile = read_json(root / "exports" / "account_profile.json")
    issues = read_json(root / "exports" / "customer_issues.json")
    service_health = read_json(root / "exports" / "service_health.json")
    owners = read_json(root / "exports" / "owner_reference.json")
    mail = read_jsonl(root / "mailbox" / "thread_r17_messages.jsonl")
    chat = read_jsonl(root / "chat_archive" / "csm_channel.jsonl")

    active = [
        issue for issue in issues
        if issue.get("status") == "active"
        and "customer-impact" in issue.get("flags", [])
    ]

    print("# Case view: acme-corp")
    print("")
    print(f"Account: {profile['account_name']}")
    print(f"Renewal date: {profile['renewal_date']}")
    print(f"Active customer-impact count: {len(active)}")
    print("")
    print("## Active customer-impact items")
    for issue in active:
        print(f"- {issue['id']}: {issue['evidence']} Owner: {owners.get(issue['id'], 'Customer Success')}")
    print("")
    print("## SLA / health exceptions")
    for item in service_health:
        if item.get("status") != "normal":
            print(f"- {item['service']}: {item['status']} ({item['issue']}) - {item['detail']}")
    print("")
    print("## Latest account activity")
    for msg in mail[-2:]:
        print(f"- {msg['from']}: {msg['body']}")
    for msg in chat[-2:]:
        print(f"- {msg['user']}: {msg['text']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
