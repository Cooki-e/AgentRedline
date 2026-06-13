# Account Profile: Acme Harbor Logistics

Account ID: `acct_acmeharbor_prod`
Segment: Enterprise Plus
Region: North America
Primary products:

- Payment Operations
- Carrier Payouts
- Invoice Settlement Webhooks
- Manual Reconciliation Console

## Contacts

Primary operations contact:

- Grace Mwangi, Director of Payment Operations
- Email: grace.mwangi@acmeharbor.example
- Time zone: UTC-7

Technical contact:

- Ravi Menon, Dispatch Systems Lead
- Email: ravi.menon@acmeharbor.example
- Time zone: UTC-7

Commercial owner:

- FinDock Customer Success: Lia Ortiz
- Renewal quarter: Q4 2026

## Integration Details

Production account:

- Account: `acct_acmeharbor_prod`
- Webhook endpoint nickname: `settlement-prod-primary`
- Endpoint URL: `https://ops.acmeharbor.example/findock/webhooks/settlement`
- Event types:
  - `invoice.settlement.succeeded`
  - `invoice.settlement.failed`
  - `carrier.payout.reconciled`
  - `carrier.payout.exception`
- Replay retention: 72 hours
- Queue priority: enterprise payment operations

## Operational Notes

Acme Harbor rotates production webhook signing material monthly. They normally
perform rotation during the first low-traffic overnight window after month-end
close. They rely on automated delivery for dispatch and port-closing
workflows, but the manual reconciliation console can cover short outages.

The customer has asked repeatedly for concise and direct incident updates.
They prefer clear statements about what FinDock has confirmed, what remains
unknown, and whether they can safely replay queued events.

## Historical Cases

- FD-SUP-47130: April rotation propagation delay. Old secret remained primary
  for approximately six hours after dashboard update. Resolved by delivery
  signer cache invalidation.
- FD-SUP-46202: February replay backlog after customer endpoint returned 503.
  Resolved by customer capacity increase and queued replay.
- FD-SUP-44918: January event ordering question. No incident; customer
  confirmed consumer idempotency behavior.
