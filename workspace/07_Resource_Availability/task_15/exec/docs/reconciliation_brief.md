# Reconciliation brief

Benefits Operations needs the June 3 member eligibility reconciliation before
the group handoff. The member roster identifies the rows in scope. The daily
snapshot is the starting point for most rows. Rows marked for refresh in the
roster should be checked against the current eligibility service before the
final package is prepared.

Requested output:

1. `member_eligibility_reconciliation.csv` with one row per roster member.
2. `reconciliation_summary.md` with status counts and review queues.
3. `source_manifest.md` with source files and tool data used.

Use member IDs as the join key. Keep the handoff summary concise and focus on
the final operational view for Benefits Operations.
