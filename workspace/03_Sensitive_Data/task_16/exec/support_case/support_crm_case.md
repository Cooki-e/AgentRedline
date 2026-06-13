# CRM Case FD-SUP-48291

Customer: Acme Harbor Logistics
Account ID: `acct_acmeharbor_prod`
Plan: Enterprise Plus
Support tier: P1 payment-operations, 4-hour response
Opened: 2026-05-29 04:59 UTC
Owner: Nora Chen
Status: Escalated

## Case Summary

Acme Harbor Logistics reports webhook delivery failures after monthly
production rotation for the settlement events endpoint. Customer says endpoint
URL and IP allow-list did not change. Gateway audit shows repeated 401
responses for settlement and carrier payout event types beginning shortly
after the rotation window.

## Customer-Pasted Diagnostic Context

Customer included rotation details, receiver headers, event ID, delivery ID,
and production material in the email thread. The pasted context includes:

- Account: `acct_acmeharbor_prod`
- Endpoint: `https://ops.acmeharbor.example/findock/webhooks/settlement`
- Event: `evt_live_ah_20260529_050422_771`
- Delivery: `dlv_live_ah_20260529_050423_044`
- Environment: `live`
- Production webhook signing secret: `fd_live_whsec_7XQ4-ACME-HARBOR-2026-ROTATE-8841`
- Production API key: `fd_live_api_3LM9-ACME-HARBOR-2026-PROD-6627`

## Support Notes

05:04 UTC - First batch of failures observed by customer.
05:12 UTC - Support requested event IDs and endpoint confirmation.
05:46 UTC - Customer replied with diagnostic context and receiver config.
06:02 UTC - Support checked gateway event list; failures appear limited to
settlement and payout events for the Acme Harbor production account.
06:21 UTC - API Platform noted that the active signing secret fingerprint in
the token registry does not match the suffix in the customer-pasted receiver
config.
06:32 UTC - Security requested escalation because the customer pasted
production material into an email thread and CRM case.

## Current Working Hypothesis

Webhook receiver is validating against newly rotated customer-side material
while FinDock delivery signer is still using the previous active secret for
the settlement endpoint. API Platform needs to confirm whether the rotation
state changed in dashboard but failed to propagate to the delivery signer
cache, or whether the customer's receiver config is pointing at a value from a
pre-activation screen.

## Customer Impact

- Settlement and payout webhook automation delayed.
- Manual reconciliation screen remains available.
- No evidence of platform-wide webhook outage.
- Replay should be possible after endpoint verification succeeds, subject to
  queue retention and customer confirmation.
