# API Platform Notes

Prepared by: Priya Shah
Time: 2026-05-29 07:18 UTC

## Current Diagnosis

The Acme Harbor failures are endpoint-specific. Control accounts delivered
successfully during the same time window, and the delivery service did not show
queue-wide errors. Gateway audit rows show customer receiver 401 responses
after the customer's rotation window.

The token registry shows dashboard active fingerprint `whfp_new_8841`, but the
delivery signer cache fingerprint remains `whfp_prev_19c8`. That mismatch
matches the customer's observed verification failure pattern.

## Suspected Product Gap

The Enterprise Dashboard bulk settings path emits `dashboard_applied` but may
not emit the same signer cache invalidation event as the primary endpoint
rotation path. The April fix did not include explicit regression coverage for
bulk settings.

## Proposed Platform Action

1. Confirm the bulk settings path event trace for
   `rot_evt_20260529_043033_acmeharbor`.
2. Invalidate signer cache for endpoint `settlement-prod-primary`.
3. Ask Support to have the customer rotate replacement material and update
   their receiver.
4. Send a test event after the customer confirms receiver update.
5. Replay affected settlement and payout events after test success.

## Notes for Support

This is not a general FinDock webhook outage. The evidence points to an
endpoint-specific signing-state mismatch after rotation. The customer can keep
using the manual reconciliation console while the webhook queue is held. Queue
retention is sufficient for a replay if the endpoint is verified today.
