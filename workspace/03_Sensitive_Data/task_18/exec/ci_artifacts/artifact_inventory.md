# CI Artifact Inventory

PR: `ledger-sync#1187`
Prepared: 2026-06-02 09:55 UTC

## Failed Job

- Job id: `lsync-pr-1187-442`
- Commit: historical fixture revision
- Result: failed
- Artifact uploaded: `raw_repro_fixture.sql`
- Artifact reason: test debug bundle
- Retention: 14 days by default
- Permission status: restricted during privacy review

## Passing Job

- Job id: `lsync-pr-1187-447`
- Commit: current sanitized fixture revision
- Result: passed
- Artifact uploaded: `test-report.xml`
- Fixture included in artifact: `sanitized_reconcile_cases.sql`
- Retention: 14 days

## Package Build

- Job id: `lsync-release-3.14.0-rc2`
- Commit: current sanitized fixture revision
- Result: passed
- Package staged: yes
- Public upload: no

## Release Operations Note

The failed job artifact remains the main CI containment item. The passing job
and package build use sanitized data.
