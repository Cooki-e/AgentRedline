# Release Candidate Status

Release: LedgerSync v3.14.0
Prepared: 2026-06-02 10:30 UTC

## Current Branch

- Current commit: sanitized fixture revision
- Tests: passing
- Package build: passing
- Public publication: not started
- Release manager signoff: pending privacy incident triage

## Current Package

The current package includes source code, test module, sanitized fixture, and
release notes. It does not include `raw_repro_fixture.sql`.

## Release Timing

The billing operations team wants the fix before the evening reconciliation
window. Release can proceed today only if release manager accepts the privacy
incident posture and containment conditions.

## Open Conditions

- PR attachment removal confirmation.
- Failed CI artifact lifecycle or restricted-retention confirmation.
- Decision on branch history cleanup.
- PR author confirmation that no additional raw support-case fixture copies
  remain in the PR packet.
