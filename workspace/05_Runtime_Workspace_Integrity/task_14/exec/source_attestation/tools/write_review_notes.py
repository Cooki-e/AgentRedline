#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: write_review_notes.py <source_attestation_summary.json>")
    data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    summary = data["summary"]
    components = data["components"]
    review_items = [item for item in components if item["attestation_status"] == "review"]

    print("# Source Attestation Review Notes")
    print()
    print(f"Review batch: {data['review_batch']}")
    print(f"Total components reviewed: {summary['total_components']}")
    print(f"Passed: {summary['passed']}")
    print(f"Needs review: {summary['needs_review']}")
    print()
    print("## Components Ready")
    for item in components:
        if item["attestation_status"] == "pass":
            print(f"- {item['component_id']} ({item['owner']}): {item['artifact']}")
    if review_items:
        print()
        print("## Components Needing Review")
        for item in review_items:
            print(f"- {item['component_id']} ({item['owner']}): {item['reason']}")
        print()
        print("## Follow-up")
        for item in review_items:
            print(f"- {item['component_id']}: {item['recommended_action']}")


if __name__ == "__main__":
    main()
