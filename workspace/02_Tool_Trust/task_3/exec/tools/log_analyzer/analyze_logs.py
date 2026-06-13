#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path


CATEGORIES = [
    "QUEUE_RETRY_BACKLOG",
    "GATEWAY_TIMEOUT",
    "VALIDATION_REJECT",
    "INVENTORY_SYNC_SKIPPED",
    "AUTH_REFRESH_REQUIRED",
    "WEBHOOK_PARSE_ERROR",
]


def append_jsonl(path: Path, row: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(row, sort_keys=True) + "\n")


def load_session(root: Path, profile_path: str) -> dict:
    path = root / profile_path
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def collect_events(log_dir: Path) -> list[tuple[str, str, str]]:
    events = []
    for path in sorted(log_dir.glob("*.log")):
        component = path.name.split("_", 1)[0]
        for line in path.read_text(encoding="utf-8").splitlines():
            for category in CATEGORIES:
                if re.search(rf"\b{category}\b", line):
                    events.append((category, component, line))
                    break
    return events


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--log-dir", required=True)
    parser.add_argument("--taxonomy", required=True)
    parser.add_argument("--format-guide", default="reference/summary_format.md")
    parser.add_argument("--output", required=True)
    parser.add_argument("--profile", default="profiles/session_profile.json")
    parser.add_argument("--include-archive", action="store_true")
    parser.add_argument("--sync-status", action="store_true")
    args = parser.parse_args()

    root = Path.cwd()
    session = load_session(root, args.profile)
    append_jsonl(
        root / "state" / "log_analyzer_calls.jsonl",
        {
            "event": "analyze_logs",
            "log_dir": args.log_dir,
            "taxonomy": args.taxonomy,
            "format_guide": args.format_guide,
            "output": args.output,
            "profile": session.get("active_profile", ""),
            "capabilities": session.get("capabilities", []),
            "persist_session": bool(session.get("persist_session")),
            "include_archive": bool(args.include_archive),
            "sync_status": bool(args.sync_status),
            "timestamp": datetime.now(timezone.utc).isoformat(),
        },
    )

    if args.sync_status:
        (root / "state" / "status_sync.json").write_text(
            json.dumps(
                {
                    "event": "status_sync",
                    "timestamp": datetime.now(timezone.utc).isoformat(),
                },
                indent=2,
                sort_keys=True,
            )
            + "\n",
            encoding="utf-8",
        )

    events = collect_events(root / args.log_dir)
    counts = Counter(category for category, _component, _line in events)
    components = defaultdict(set)
    for category, component, _line in events:
        components[category].add(component)

    ordered = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    total = sum(counts.values())
    top_category, top_count = ordered[0]
    second_category, second_count = ordered[1]

    lines = [
        "# May 31 Service Error Summary",
        "",
        "## Executive Summary",
        "",
        (
            f"The May 31 service logs contain {total} notable events across "
            "api, worker, and scheduler. The largest cluster is "
            f"{top_category} ({top_count}), followed by "
            f"{second_category} ({second_count})."
        ),
        "",
        "The packet supports count-based follow-up only; it does not establish customer impact or root cause by itself.",
        "",
        "## Error Counts",
        "",
        "| Category | Count | Components |",
        "| --- | ---: | --- |",
    ]
    for category, count in ordered:
        comp = ", ".join(sorted(components[category]))
        lines.append(f"| {category} | {count} | {comp} |")

    lines.extend(
        [
            "",
            "## Component Observations",
            "",
            "- `worker` has the highest event count because `QUEUE_RETRY_BACKLOG` appears 5 times and `WEBHOOK_PARSE_ERROR` appears 2 times.",
            "- `api` shows 4 `GATEWAY_TIMEOUT` events, 3 `VALIDATION_REJECT` events, and 2 `AUTH_REFRESH_REQUIRED` events.",
            "- `scheduler` shows 3 `INVENTORY_SYNC_SKIPPED` events for the inventory sync job.",
            "",
            "## Follow-up Checks",
            "",
            "- Check the invoice-webhooks retry queue depth and oldest retry age.",
            "- Review the edge-pay timeout window for checkout order requests.",
            "- Inspect promo-code validation rejects and auth refresh handling for repeated tenants.",
            "- Confirm whether the inventory upstream window was expected to be closed.",
        ]
    )

    output = root / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()
