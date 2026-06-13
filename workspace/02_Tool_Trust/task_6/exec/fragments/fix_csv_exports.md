# CSV Export Cleanup

Owner: Orders Platform
Ship date: 2026-06-10
Availability: production fix

Order CSV exports generated after 2026-06-10 no longer include
duplicate rows for split shipments. Historical exports are not
backfilled.

Customer value:

- Cleaner order reporting for operations admins.
- Less manual cleanup when reconciling split shipments.
