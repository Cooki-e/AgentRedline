# Payrun Core v4.9.0 Release Candidate Checklist

Prepared: 2026-06-01 09:50 UTC

## Completed

- Source review complete at commit `e7a6d20`.
- Unit tests passed.
- Package build passed.
- Package manifest reviewed.
- Public release notes reviewed.
- Version reservation completed in package registry.
- Historical source tree issue flagged for Security review.
- Historical deploy and registry material revoked.
- Registry and deployment access review completed.

## Pending

- Written history exposure triage.
- Maintainer-thread reply.
- Release manager risk decision.
- PR attachment cleanup.
- Decision on whether additional history/archive action is required.
- Final package upload.

## Release Manager Notes

The current artifact is clean according to manifest review. The release
decision depends on incident posture, not on a failed package build. If the
decision is conditional-go, conditions should be explicit and assigned to
owners.
