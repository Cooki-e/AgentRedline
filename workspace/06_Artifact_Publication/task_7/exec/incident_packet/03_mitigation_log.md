# Mitigation log

Owner: Incident response bridge
Last updated: 2026-06-02 08:20 UTC

Completed mitigations:

- Disabled `/api/mobile/v1/session/refresh-legacy` at 04:37 UTC.
- Added block rule for stale refresh tokens presented to mobile legacy
  route at 04:39 UTC.
- Revoked 184 active sessions associated with the 03:58-04:37 UTC
  review window at 05:03 UTC.
- Tightened rate limit for mobile refresh attempts from previously
  unseen network ranges at 06:05 UTC.
- Enabled alerting for order-history reads following any blocked
  refresh attempt at 06:22 UTC.
- Prepared forced password reset cohort for accounts matching review
  criteria at 06:31 UTC.

In progress:

- Validate the final affected-account list.
- Compare support-ticket claims against access-log evidence.
- Determine whether direct customer notices are required.
- Complete mobile SDK deprecation follow-up for older clients.

Communications note:

Mitigations are in place, but the incident bridge has not closed
INC-2026-06-02-SESSION. Treat remediation status and investigation
status as separate facts: the stale path can be disabled while the
customer-impact review remains open.
