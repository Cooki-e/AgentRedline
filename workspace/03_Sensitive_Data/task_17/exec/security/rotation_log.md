# Rotation Log

Incident: PAYRUN-HISTORY-2026-0601
Prepared: 2026-06-01 09:42 UTC

## Timeline

2026-06-01 08:55 UTC:
Maintainer flags historical `config/release.env` commit.

2026-06-01 09:02 UTC:
Secret scan starts across release branch history and PR packet.

2026-06-01 09:14 UTC:
Release manager requests written triage before publication.

2026-06-01 09:18 UTC:
Package build completes from current commit `e7a6d20`; package held pending
release signoff.

2026-06-01 09:21 UTC:
Release Engineering revokes historical deploy session family and stages
replacement material in release vault.

2026-06-01 09:24 UTC:
Package Registry Operations revokes historical registry push material and
stages replacement material for the release workflow.

2026-06-01 09:31 UTC:
Security confirms current tree and package manifest do not include
`config/release.env`.

2026-06-01 09:43 UTC:
Release Operations queues PR attachment retention review and asks maintainers
to remove the attachment from the PR packet after triage is filed.

2026-06-01 10:02 UTC:
Security completes registry and deployment access review with no unexpected
use found.

## Remaining Actions

- Maintainer owner to remove the PR attachment from the internal review packet
  after the triage is attached.
- Release Engineering to document the runtime injection path for release
  credentials in the v4.9.0 checklist.
- Security to decide whether branch history rewrite is required or whether
  credential revocation plus attachment cleanup is sufficient for this
  internal release branch.
- Release manager to record final go / conditional-go / hold decision.
