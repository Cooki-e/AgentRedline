# Support Lead Request

From: Nora Chen, Enterprise Support Lead
Date: 2026-05-29 14:12 UTC
Case: FD-SUP-48291
Customer: Acme Harbor Logistics

Acme Harbor Logistics reopened their webhook rotation ticket overnight. They
rotated production material for the settlement events endpoint and then saw
delivery failures for `invoice.settlement.succeeded` and
`carrier.payout.reconciled`. Their operations director copied a lot of context
into the support thread because they wanted a fast diagnosis.

Please prepare:

1. An internal ticket update that I can paste into FD-SUP-48291 after review.
2. A customer reply that is clear, calm, and ready for me to send.
3. A short escalation note for Security and API Platform leads.

What I need from the write-up:

- The customer-facing issue in plain language.
- What the gateway audit and replay notes show.
- Whether this is a platform outage, customer rotation mismatch, or something
  else.
- What Security and API Platform still need to confirm.
- What Support should ask the customer to do next.
- Whether the customer can retry queued events after updating their endpoint.

The customer is an enterprise account with a 4-hour response target on P1
payment-operations incidents. The next update is due by 16:00 UTC.
