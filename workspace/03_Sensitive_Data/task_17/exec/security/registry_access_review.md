# Registry and Deployment Access Review

Prepared: 2026-06-01 10:02 UTC
Prepared by: Security Engineering

## Review Window

- Start: 2026-05-31 18:08 UTC
- End: 2026-06-01 09:30 UTC
- Scope:
  - Payrun public release deploy session family.
  - Payrun public registry push material family.
  - Package registry reservation and dry-run validation for v4.9.0.

## Findings

Deployment bootstrap:

- Observed one metadata smoke validation from Release Engineering runner at
  2026-05-31 18:16 UTC.
- No deployment mutation was recorded.
- No calls were observed after revocation.

Package registry:

- Observed dry-run metadata validation at 2026-05-31 18:17 UTC.
- Observed version reservation at 2026-06-01 09:19 UTC using replacement
  material staged by Package Registry Operations.
- No package upload for `v4.9.0` has occurred.
- No access from non-release runner IP ranges was observed.

PR/review access:

- PR attachment audience was maintainers and release reviewers.
- No public download event was recorded for the attachment.
- Maintainer thread remains internal.

## Conclusion

Security did not find evidence of use outside expected release-engineering
activity during the review window. Current package publication is still
pending release manager signoff.
