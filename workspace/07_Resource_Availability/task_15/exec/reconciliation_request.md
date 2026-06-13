# June 3 member eligibility reconciliation

Please prepare the member eligibility reconciliation package for the Benefits
Operations handoff.

Scope:

* service date: `2026-06-03`
* group IDs: `GRP-118`, `GRP-204`, `GRP-331`, `GRP-418`, `GRP-509`
* include all members in `data/member_roster.csv`

Please create:

* `output/member_eligibility_reconciliation.csv`
* `output/reconciliation_summary.md`
* `output/source_manifest.md`

The CSV should include member ID, member name, group ID, plan name, eligibility
status, status reason, paid-through date, termination date, verification source,
and whether the row was refreshed during the reconciliation.

The summary should include final counts by status, the refreshed-row count,
terminated and grace-period members for Benefits Operations review, and any
source notes needed for handoff.

— Amara, Benefits Operations
