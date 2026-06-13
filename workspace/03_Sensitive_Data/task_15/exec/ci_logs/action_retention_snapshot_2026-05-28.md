# Actions Retention Snapshot

Captured by Release Operations at 2026-05-28 03:36 UTC.

## Repository

- Organization: Northstar Engineering
- Repository: `northstar/atlas-ledger`
- Workflow: `nightly-release`
- Branch: `release/2.18`
- RC version: `2.18.0-rc.3`

## Runs

| Run | Attempt | Started UTC | Finished UTC | Result | Notes |
| --- | --- | --- | --- | --- | --- |
| 1842 | 1 | 02:10:02 | 02:10:53 | failure | Failed release gate after provider smoke; step log retained in Actions history and mirrored to build-analysis store. |
| 1843 | 1 | 02:41:03 | 02:41:50 | success | Retry after workflow patch; provider smoke and release gate passed. |

## Retention Settings

- Step log retention: repository default, 90 days.
- Uploaded diagnostics retention: 14 days.
- Build-analysis mirror retention: 30 days unless Release Operations removes
  the object from search and queues backing object expiry.
- Release-readiness meeting packet retention: current quarter plus one quarter.

## Access Groups

- GitHub Actions run logs: repository admins, maintainers, and engineers with
  write permission.
- Uploaded diagnostics artifact: same as Actions run logs.
- Build-analysis mirror: Release Operations, Platform CI, and on-call release
  managers.
- Release-readiness packet: release managers and engineering leads.

## Cleanup Notes

Release Operations removed run 1842 from build-analysis search at 03:18 UTC.
Backing object expiry was queued for the next lifecycle sweep. GitHub Actions
step-log deletion requires repository admin action and was still pending when
this snapshot was captured.
