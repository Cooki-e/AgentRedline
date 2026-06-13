#!/usr/bin/env python3
from __future__ import annotations

import json


def main() -> None:
    manifest = {
        "sources": [
            "portal_visual_audit/README.md",
            "portal_visual_audit/docs/handoff_request.md",
            "portal_visual_audit/docs/release_review_notes.md",
            "portal_visual_audit/docs/browser_audit_runbook.md",
            "portal_visual_audit/audit_inputs/route_manifest.csv",
            "portal_visual_audit/audit_inputs/known_issues.csv",
            "portal_visual_audit/audit_inputs/release_owner_matrix.csv",
            "portal_visual_audit/reference/release_criteria.csv",
            "portal_visual_audit/reference/design_tokens.json",
            "portal_visual_audit/snapshots/routes/home.html",
            "portal_visual_audit/snapshots/routes/billing.html",
            "portal_visual_audit/snapshots/routes/support.html",
            "portal_visual_audit/snapshots/routes/settings.html",
            "portal_visual_audit/snapshots/routes/reports.html",
            "portal_visual_audit/snapshots/routes/admin.html",
        ],
        "generated_outputs": [
            "results/route_audit_summary.json",
            "results/visual_issue_register.csv",
            "results/audit_notes.md",
            "results/source_manifest.json",
        ],
    }
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
