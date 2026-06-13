#!/usr/bin/env python3
from __future__ import annotations

import json


def main() -> None:
    manifest = {
        "sources": [
            "trial_query_resolution/README.md",
            "trial_query_resolution/docs/handoff_request.md",
            "trial_query_resolution/docs/data_management_notes.md",
            "trial_query_resolution/docs/closeout_playbook.md",
            "trial_query_resolution/source_data/subjects.csv",
            "trial_query_resolution/source_data/labs.csv",
            "trial_query_resolution/source_data/adverse_events.jsonl",
            "trial_query_resolution/source_data/site_notes.md",
            "trial_query_resolution/reference/protocol_windows.csv",
            "trial_query_resolution/reference/lab_thresholds.csv",
            "trial_query_resolution/reference/query_severity_map.csv",
        ],
        "generated_outputs": [
            "results/query_listing.csv",
            "results/query_summary.md",
            "results/source_manifest.json",
        ],
    }
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
