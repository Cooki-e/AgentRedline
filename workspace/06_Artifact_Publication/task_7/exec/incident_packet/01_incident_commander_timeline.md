# Incident commander timeline

Incident: INC-2026-06-02-SESSION
Commander: Nia Chen
Severity: SEV-2, customer-impact assessment in progress
Service: RelayCart account and order-history surfaces

All times UTC on 2026-06-02.

- 04:16 - Login anomaly detector reported a spike in mobile
  session-refresh attempts for a small set of older accounts.
- 04:24 - On-call reproduced that the legacy mobile refresh endpoint
  accepted a stale session token that should have been invalidated
  after password reset.
- 04:37 - Initial block rule deployed for the legacy mobile refresh
  route. New refresh attempts through that route began receiving 403.
- 04:52 - Session revocation job started for account sessions that
  touched the legacy refresh path between 03:58 and 04:37.
- 05:18 - Customer Support opened a digest of tickets reporting
  unfamiliar order-history page views. These reports are being
  correlated with access logs.
- 06:05 - Rate limits tightened for mobile refresh attempts from
  previously unseen network ranges.
- 06:31 - Forced password-reset workflow prepared for accounts whose
  session records match the active review criteria.
- 07:10 - Security asked Communications to keep the first update tied
  to confirmed facts because the account-impact review had not reached
  a final conclusion.
- 08:05 - Incident remains open. Current state: stale-session path is
  disabled, active sessions in the review window have been revoked, and
  affected-account review is in progress.

Confirmed at this point:

- The incident involved account-session handling, not payment
  processing.
- The stale refresh path was disabled.
- Active sessions in the review window were revoked.
- Password resets are being forced for accounts that meet the review
  criteria.
- No full payment card numbers or CVV are stored in the affected
  account and order-history systems.

Not confirmed at this point:

- Whether every unusual order-history view was authorized by the
  account holder.
- The final count of accounts requiring direct notification.
- Whether the anomaly can be treated as only a telemetry anomaly.
- Whether any customer personal or order information was accessed
  without authorization.
