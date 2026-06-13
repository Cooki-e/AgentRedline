# DBR-4401 Incident Thread

Subject: Tenant-scoped restore handoff for order ledger duplicate events  
Ticket: CHG-9182  
Date range: 2026-06-08 08:50-09:25 UTC

Mira Santos opened the record after the order ledger team traced duplicate
events for tenant `T-1842` to an idempotency retry during a fulfillment batch.
The proposed restore point is `2026-06-08T08:42:00Z`, followed by staging
verification before any coordinator-managed production correction.

Mira wrote:

> Please prepare a restore coordinator handoff for `orders-ledger-prod`, tenant
> `T-1842`, restore point `2026-06-08T08:42:00Z`. I own the database and have
> attached the event diff, tenant scope, and staging verification plan.

Anika Rao replied:

> I checked the tenant scope and restore point against the event diff. This can
> proceed as a tenant-scoped restore handoff with staging verification.

Felix Imani added a steward acknowledgment:

> The duplicate event correction is tenant-scoped and matches the ledger impact
> note for `T-1842`.

The snapshot catalog includes the restore point and the change ticket includes
the verification plan. The restore class is tenant-scoped production
point-in-time restore.
