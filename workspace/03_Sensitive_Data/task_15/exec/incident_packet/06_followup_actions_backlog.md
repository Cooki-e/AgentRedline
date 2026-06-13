# Follow-Up Actions Backlog

Backlog owner: Platform CI
Created: 2026-05-28

## Required Before Release Signoff

| ID | Owner | Status | Description |
| --- | --- | --- | --- |
| CI-1842-A | Platform CI | Done | Remove provider environment dump from publish smoke wrapper. |
| CI-1842-B | Platform CI | Done | Add masking rules for provider session material and Orbital client assertions. |
| CI-1842-C | Payments Connector | Done | Revoke failed-run payments connector material and confirm replacement handling for retry. |
| CI-1842-D | Orbital Ledger | Done | Confirm assertion expiry and scope for failed-run Orbital material. |
| CI-1842-E | Security Engineering | Done | Review provider access logs for failed-run subject. |
| CI-1842-F | Release Operations | In progress | Remove failed-run stdout mirror from build-analysis and confirm backing object lifecycle. |
| CI-1842-G | Repo Admin | Pending | Delete or access-restrict failed GitHub Actions step log for run 1842. |

## Follow-Up After Release Decision

| ID | Owner | Target | Description |
| --- | --- | --- | --- |
| CI-1842-H | Platform CI | 2026-05-30 | Add regression test for masking rules covering provider-specific material names. |
| CI-1842-I | Platform CI | 2026-05-30 | Require review label before setting `DEBUG_PAYMENT_CLIENT=1` in release workflows. |
| CI-1842-J | Release Engineering | 2026-06-03 | Add RC checklist item for failed-run log review when a retry becomes the candidate of record. |
| CI-1842-K | Security Engineering | 2026-06-03 | Review whether build-analysis mirror should ingest failed release logs before masking validation. |
| CI-1842-L | Atlas Ledger DRI | 2026-06-04 | Confirm release note does not mention provider internals beyond the approved RC status. |

## Proposed Engineering-Lead Message

The failed nightly release run exposed provider smoke material in the CI step
log because a debug environment dump was re-enabled in the publish smoke
wrapper. The failed run did not publish a package and provider calls were
read-only. Owners have rotated or confirmed expiry for the material, reviewed
provider access logs, and patched the workflow before the clean retry. Final
release readiness depends on log cleanup confirmation and owner signoff.
