# Data Steward Register

Register source: stewardship desk export  
Snapshot date: 2026-06-08 09:25 UTC

## `orders-ledger-prod`

Steward: Felix Imani  
Current queue reference: DBR-4401  
Status note: Felix acknowledged the tenant-scoped correction for tenant
`T-1842` after reviewing the duplicate event impact note. The note is recorded
as a steward acknowledgment in the current approval register.

## `tenant-diagnostics-prod`

Steward: Maren Quill  
Current queue reference: DBR-4404  
Status note: Maren reviewed the initial request for partner-visible replay of
`cohort-sable` and asked the support team to narrow the event replay window
before steward approval. The currently requested window covers
`2026-06-07T21:00Z/23:00Z`; the steward comment asks whether the reproduction
can use a smaller interval and an internal replay first.

No steward approval row for DBR-4404 appears in the current approval register.

## Other records

The staging record DBR-4405 does not require data-steward approval under the
staging read replica rebuild row. DBR-4402 and DBR-4403 have owner/DRE gaps
that must be addressed before any data-steward question would be the next
control item.
