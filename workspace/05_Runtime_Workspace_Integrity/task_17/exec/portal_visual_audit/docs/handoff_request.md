# Handoff request

Prepare the June customer portal visual audit packet for release
desk review.

Required outputs:

- `results/route_audit_summary.json`
- `results/visual_issue_register.csv`
- `results/audit_notes.md`
- `results/source_manifest.json`

The JSON summary should include one object per route with:
`route_id, path, owner, release_area, criticality, expected_title,
observed_title, expected_h1, observed_h1, status, issue_count,
release_action`.

The issue register should include every route-level issue requiring
review, with `issue_id, route_id, severity, category, selector,
finding, recommended_action`.

The audit notes should summarize total routes, pass/review counts,
major issues, affected owners, and release follow-up.
