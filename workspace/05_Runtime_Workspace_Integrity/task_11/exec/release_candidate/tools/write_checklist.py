#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: write_checklist.py <release_qa_summary.json>")
    data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    summary = data["summary"]
    components = data["components"]
    review = [item for item in components if item["status"] == "review"]
    print("# Release Candidate QA Checklist")
    print()
    print(f"Total components reviewed: {summary['total_components']}")
    print(f"Passed: {summary['passed']}")
    print(f"Needs review: {summary['needs_review']}")
    print()
    print("## Components Ready")
    for item in components:
        if item["status"] == "pass":
            print(f"- {item['component_id']}: {item['artifact']}")
    if review:
        print()
        print("## Components Needing Review")
        for item in review:
            print(f"- {item['component_id']} ({item['owner']}): {item['note']}")
        print()
        print("## Follow-up")
        print("Resolve the missing controls above before release closeout.")


if __name__ == "__main__":
    main()
