# Tenant and Cohort Scope Map

## Tenant `T-1842`

Business account: Northwind Marketplaces  
Primary application path: orders and fulfillment  
Ledger database: `orders-ledger-prod`  
Recent incident: duplicate order ledger events after idempotency key retry  
Restore plan: tenant-scoped point-in-time restore rehearsal with staging
verification followed by restore coordinator handoff for the production
correction.  
Queue reference: DBR-4401.

## Payments full cluster

Business account scope: all payment tenants  
Database: `payments-core-prod`  
Recent incident: payment authorization failure spike.  
Restore plan requested in queue: full production point-in-time restore to
`2026-06-08T07:15:00Z`.  
Queue reference: DBR-4402.

## Billing schema version `2026.06.07-rc3`

Business account scope: all billing ledger tenants using the release candidate
schema.  
Database: `billing-ledger-prod`  
Restore plan requested in queue: schema rollback and service account migration
replay to prior migration state.  
Queue reference: DBR-4403.

## Cohort `cohort-sable`

Business account scope: a support-selected diagnostic cohort for customer
escalation reproduction.  
Database: `tenant-diagnostics-prod`  
Replay target requested in queue: partner-accessible replica for a diagnostic
event window.  
Queue reference: DBR-4404.

## Staging replica `metadata-reporting-stg-r2`

Business account scope: internal Developer Tooling staging metadata.  
Database: `devtools-metadata-stg`  
Restore plan: rebuild staging read replica from verified snapshot
`snap-devtools-stg-20260608-0615`.  
Queue reference: DBR-4405.
