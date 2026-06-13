# Provider Access Log Review

Prepared: 2026-05-28 06:12 UTC
Prepared by: Security Engineering
Inputs: provider audit queries from Payments Connector and Orbital Ledger

## Payments Connector Query

Query id: `pay-audit-2026-0528-1842`
Window: 2026-05-28 02:10 UTC through 2026-05-28 03:05 UTC
Subject: `gha:nightly-release:1842`

Observed calls:

| Time UTC | Endpoint | Result | Request ID |
| --- | --- | --- | --- |
| 02:10:48 | settlement-window list | 200 | psmk-1842-7ac2 |
| 02:10:49 | currency-table read | 200 | psmk-1842-7ad1 |
| 02:10:49 | account-mode read | 200 | psmk-1842-7ad8 |

No calls were observed after the provider smoke step. No calls were observed
from a source outside GitHub-hosted runner egress for the workflow. No write
endpoints were called. No customer payment instrument endpoints were called.

Revocation confirmation:

- Revocation request accepted at 03:02 UTC.
- Post-revocation test request using the same subject class returned 401 in
  the owner team's validation.

## Orbital Ledger Query

Query id: `orb-access-2026-0528-1842`
Window: 2026-05-28 02:10 UTC through 2026-05-28 02:45 UTC
Subject: `gha:nightly-release:1842`

Observed calls:

| Time UTC | Endpoint | Result | Request ID |
| --- | --- | --- | --- |
| 02:10:49 | environment metadata | 200 | orb-1842-19d0 |
| 02:10:50 | invoice schema version | 200 | orb-1842-19dc |
| 02:10:50 | reconciliation compatibility | 200 | orb-1842-19e2 |

No calls were observed after the assertion expiry time. No invoice contents,
ledger entries, or write endpoints were accessed.

## Build System Review

Release Operations reviewed:

- Uploaded diagnostics artifact for failed run 1842.
- Build-analysis mirror object metadata.
- Retry run 1843 stdout.
- Release-readiness packet draft.

Findings:

- Failed step log and build-analysis stdout mirror were the only locations
  known to contain the provider environment dump.
- Uploaded diagnostics artifact did not contain provider environment material.
- Retry run 1843 did not print provider environment material.
- Release-readiness packet had not yet been finalized at the time of review.
