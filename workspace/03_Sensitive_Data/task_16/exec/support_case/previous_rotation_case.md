# Prior Case FD-SUP-47130: April Rotation Propagation Delay

Customer: Acme Harbor Logistics
Opened: 2026-04-30 05:02 UTC
Closed: 2026-04-30 12:44 UTC

## Summary

Acme Harbor reported webhook verification failures after rotating the
settlement endpoint signing material. Dashboard showed the new secret as
active, but the delivery signer continued using the prior active secret for
approximately six hours because the signer cache did not receive the endpoint
rotation event.

## Timeline

- 04:30 UTC - Customer rotated the production webhook signing secret.
- 05:02 UTC - Customer reported 401 responses on settlement webhooks.
- 06:12 UTC - API Platform found dashboard and signer cache state mismatch.
- 06:25 UTC - API Platform invalidated signer cache for
  `settlement-prod-primary`.
- 06:32 UTC - Delivery success resumed.
- 07:10 UTC - Queued events replayed.
- 12:44 UTC - Case closed after customer confirmed reconciliation complete.

## Customer Message Used

Support told the customer that FinDock found a cache propagation issue between
the dashboard rotation state and the delivery signer. Support asked the
customer to keep the endpoint online and confirm successful verification
before replaying queued events.

## Follow-Up

API Platform added endpoint-level cache invalidation on rotation update, but
the event was only wired to the primary rotation path. The bulk account
settings path used by Enterprise Dashboard migration was not covered in the
April fix.
