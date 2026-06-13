#!/usr/bin/env python3
from __future__ import annotations

import json


def main() -> None:
    manifest = {
        "sources": [
            "source_attestation/README.md",
            "source_attestation/docs/handoff_request.md",
            "source_attestation/docs/status_runbook.md",
            "source_attestation/docs/attestation_policy_notes.md",
            "source_attestation/records/components.csv",
            "source_attestation/records/repository_status.csv",
            "source_attestation/records/artifact_manifest.csv",
            "source_attestation/records/approvals.csv",
            "source_attestation/policy/attestation_controls.csv",
            "source_attestation/tools/evaluate_source_attestations.py",
            "source_attestation/tools/write_review_notes.py",
        ],
        "generated_outputs": [
            "results/source_attestation_summary.json",
            "results/review_notes.md",
            "results/source_manifest.json",
        ],
    }
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
