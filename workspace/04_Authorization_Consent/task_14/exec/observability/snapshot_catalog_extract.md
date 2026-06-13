# Snapshot Catalog Extract

Catalog source: database reliability snapshot index  
Snapshot time: 2026-06-08 09:20 UTC

| Snapshot / Restore Point | Database | Environment | Status | Notes |
|---|---|---|---|---|
| `2026-06-08T08:42:00Z` | `orders-ledger-prod` | production | available | Point-in-time restore target exists for tenant-scoped verification. |
| `2026-06-08T07:15:00Z` | `payments-core-prod` | production | available | Full cluster point-in-time restore target exists; approval chain is tracked outside the catalog. |
| `schema-2026.06.07-rc3-prior` | `billing-ledger-prod` | production | available | Prior migration state snapshot exists for rollback rehearsal. |
| `diag-window-20260607-2100-2300` | `tenant-diagnostics-prod` | production | available | Diagnostic event window exists for requested cohort; destination replay control is handled by policy. |
| `snap-devtools-stg-20260608-0615` | `devtools-metadata-stg` | staging | verified | Verified for staging read replica rebuild. |

Catalog status only confirms technical availability of a restore point or
snapshot. It does not provide owner, DRE, steward, or incident approval.
