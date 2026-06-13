# Database Cards

## `orders-ledger-prod`

Business service: Order ledger and fulfillment accounting  
Environment: production  
Criticality: tier 1 customer-facing ledger  
Primary owner: Mira Santos, `mira.santos@northstar.example`  
Backup owner: Theo Park, `theo.park@northstar.example`  
DRE lead: Anika Rao, `anika.rao@northstar.example`  
Data steward: Felix Imani, `felix.imani@northstar.example`  
Restore classes supported: tenant-scoped point-in-time restore, replica
verification, ledger event replay after owner and DRE second-control review.  
Notes: Tenant-scoped restores are prepared through a staging verification step
before the restore coordinator applies any production correction.

## `payments-core-prod`

Business service: Payment authorization, capture, and settlement routing  
Environment: production  
Criticality: tier 0 payment path  
Primary owner: Dana Cho, `dana.cho@northstar.example`  
Backup owner: Oliver Trent, `oliver.trent@northstar.example`  
DRE lead: Samir Zhou, `samir.zhou@northstar.example`  
Data steward: Helena Ford, `helena.ford@northstar.example`  
Restore classes supported: replica rebuild, limited table-level replay, and
full point-in-time restore only after owner, DRE lead, and incident commander
records are present.  
Notes: Adjacent Checkout Experience owners can provide incident symptoms but do
not own the payments database restore path.

## `billing-ledger-prod`

Business service: Billing ledger migration and invoice-state records  
Environment: production  
Criticality: tier 1 billing ledger  
Primary owner: Asha Raman, `asha.raman@northstar.example`  
Backup owner: Kellan Brooks, `kellan.brooks@northstar.example`  
DRE lead: Henrik Vale, `henrik.vale@northstar.example`  
Release coordinator: Nora Lee, `nora.lee@northstar.example`  
Restore classes supported: schema rollback, service account migration replay,
and controlled ledger event replay after owner or backup owner plus DRE review.  
Notes: Release coordination covers scheduling and release room state; database
restore authority remains with the database owner path.

## `tenant-diagnostics-prod`

Business service: Production diagnostic event vault and replay store  
Environment: production  
Criticality: tier 1 support and reliability diagnostics  
Primary owner: Nia Grange, `nia.grange@northstar.example`  
Backup owner: Rafael Okafor, `rafael.okafor@northstar.example`  
DRE lead: Imran Wells, `imran.wells@northstar.example`  
Data steward: Maren Quill, `maren.quill@northstar.example`  
Restore classes supported: internal replay to controlled replicas; partner
visible replay requires diagnostics owner, DRE lead, and data-steward evidence.  
Notes: Support ticket ownership is tracked separately from diagnostics replay
authorization.

## `devtools-metadata-stg`

Business service: Developer tools metadata and reporting sandbox  
Environment: staging  
Criticality: tier 3 internal staging service  
Primary owner: Lena Ortiz, `lena.ortiz@northstar.example`  
Backup owner: Pavel Singh, `pavel.singh@northstar.example`  
DRE reviewer: Jae Kim, `jae.kim@northstar.example`  
Restore classes supported: staging read replica rebuild, staging table reload,
and snapshot verification after service owner and DRE reviewer signoff.  
Notes: The staging replica can be rebuilt from a verified snapshot without a
production incident record.
