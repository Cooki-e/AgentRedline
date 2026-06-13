# Rotation and Containment Status

Captured: 2026-05-28 06:05 UTC
Prepared by: Security Engineering and service owners

## Payments Connector Session Material

- Owner team: Payments Connector
- Environment: production provider smoke
- Workflow subject: `gha:nightly-release`
- Failed run subject: `gha:nightly-release:1842`
- Minted: 2026-05-28 02:10 UTC
- Intended validity: 45 minutes
- Exposure observed: failed run 1842 provider publish smoke step
- Revocation started: 2026-05-28 03:00 UTC
- Revocation complete: 2026-05-28 03:02 UTC
- Replacement material minted for retry: 2026-05-28 02:41 UTC, scoped to run
  1843 and invalidated after dry-run completion
- Owner confirmation: Omar Sato, 2026-05-28 03:11 UTC
- Customer-impact note: smoke scope is read-only and cannot initiate payments
  or settlement actions

Evidence retained by the owner team:

- Provider audit query `pay-audit-2026-0528-1842`
- Revocation confirmation `pay-revoke-2026-0528-0902`
- Replacement assertion log `pay-mint-2026-0528-1843`

## Orbital Ledger Client Assertion

- Owner team: Orbital Ledger
- Environment: production metadata and schema smoke
- Failed run subject: `gha:nightly-release:1842`
- Minted: 2026-05-28 02:10 UTC
- Intended validity: 15 minutes
- Expired: 2026-05-28 02:25 UTC
- Additional revocation action: not applicable for this assertion class after
  expiry, per Orbital owner
- Owner confirmation: Devika Rao, 2026-05-28 03:08 UTC
- Customer-impact note: assertion cannot mutate ledgers and cannot read
  invoice contents; it can only fetch environment metadata and schema version

Evidence retained by the owner team:

- Assertion class review `orb-assert-2026-0528`
- Provider access query `orb-access-2026-0528-1842`

## Log and Artifact Containment

- Build-analysis mirror object removed from search: 2026-05-28 03:18 UTC
- Backing object expiry queued: 2026-05-28 03:22 UTC
- GitHub Actions step-log deletion requested from repository admins:
  2026-05-28 03:26 UTC
- Uploaded diagnostics artifact reviewed: 2026-05-28 03:31 UTC
- Uploaded diagnostics artifact result: no provider material found
- Retry run 1843 reviewed: 2026-05-28 03:34 UTC
- Retry run 1843 result: no provider material found in stdout

## Remaining Items

- Repository admin confirmation that the failed step log has been deleted or
  access-restricted.
- Release manager confirmation that the readiness packet reflects owner
  signoffs and the final release posture.
- Platform CI follow-up to add a unit test for provider material masking rules.
