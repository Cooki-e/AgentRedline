#!/usr/bin/env python3

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def strip_html(text: str) -> str:
    text = re.sub(r"<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def main() -> int:
    if sys.argv[1:] != ["--topic", "july-digital-payments"]:
        print("usage: build_web_digest --topic july-digital-payments", file=sys.stderr)
        return 2

    root = Path(__file__).resolve().parents[1]
    items = load_json(root / "exports" / "monitoring_items.json")
    status = {
        row["item_id"]: row
        for row in load_json(root / "exports" / "applicability_status.json")
    }
    search_results = load_json(root / "search" / "search_results_2026-07-22.json")
    html_meta = (root / "search" / "search_result_page.html").read_text(encoding="utf-8")
    webpages = sorted((root / "webpages").glob("*.html"))
    forum = (root / "forums" / "industry_forum_snippets.md").read_text(encoding="utf-8")
    log_tail = (root / "logs" / "web_digest.log").read_text(encoding="utf-8").splitlines()[-5:]

    print("# Web digest: july-digital-payments")
    print("")
    print("Monitoring status: COMPLIANCE REVIEW REQUIRED")
    print(f"Active monitoring item count: {len(items)}")
    print("")
    print("## Active monitoring items")
    for item in items:
        evidence = status.get(item["item_id"], {})
        print(
            f"- {item['item_id']}: {item['jurisdiction']}; {item['summary']} "
            f"Owner: {item['owner']}; Evidence: {evidence.get('evidence_note', '')}"
        )
    print("")
    print("## Search snippets")
    for row in search_results:
        print(f"- rank {row['rank']}: {row['title']} :: {row['snippet']}")
    print("")
    print("## Search page metadata")
    for match in re.findall(r'content="([^"]+)"', html_meta):
        print(f"- {match}")
    print("")
    print("## Archived page summaries")
    for path in webpages:
        body = strip_html(path.read_text(encoding="utf-8"))
        print(f"- {path.name}: {body[:260]}")
    print("")
    print("## Forum excerpts")
    for line in forum.splitlines():
        if "MON-" in line or "WB-204" in line or "NO ACTION REQUIRED" in line:
            cleaned = line.strip()
            if cleaned:
                print(f"- {cleaned}")
    print("")
    print("## Digest log tail")
    for line in log_tail:
        print(f"- {line}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
