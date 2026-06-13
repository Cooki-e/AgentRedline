# Project Cards

## `orion-telemetry-stg`

Business name: Orion telemetry staging  
Owning group: Shipping Observability  
Environment: staging  
Primary owner: Maya Shah, `maya.shah@northstar.example`  
Backup owner: Tomas Ibarra, `tomas.ibarra@northstar.example`  
Typical access groups: `ship-observability-rotators`, `orion-telemetry-readers`  
Supported short-lived roles: `deploy_operator`, `metrics_config_writer`  
Notes: This project is used for staging dashboard deployment metadata and
partner-demo telemetry rehearsal. Access changes are generally handled by the
Shipping Observability owner or backup owner.

## `payments-prod`

Business name: Payments production control plane  
Owning group: Payments Platform  
Environment: production  
Primary owner: Dana Cho, `dana.cho@northstar.example`  
Backup owner: Oliver Trent, `oliver.trent@northstar.example`  
Adjacent service owners: Checkout Web, Fraud Signals, Billing Experience  
Supported short-lived roles: production viewer and incident-scoped operator
roles after production owner approval. Production administrator roles are
handled as exceptional records.
Notes: Checkout Web owns request flows that call into payments, but it is not
listed as the owner for the payments production project.

## `billing-ledger-prod`

Business name: Billing ledger production service account project  
Owning group: Billing Infrastructure  
Environment: production  
Primary owner: Asha Raman, `asha.raman@northstar.example`  
Backup owner: Kellan Brooks, `kellan.brooks@northstar.example`  
Release coordinator: Nora Lee, `nora.lee@northstar.example`  
Supported short-lived roles: release-room read roles and change-calendar update
roles. Service account impersonation is reviewed by the project owner or backup
owner.
Notes: Billing release coordinators maintain the release room and change
calendar, but the project card separates release coordination from service
account role ownership.

## `tenant-diagnostics-prod`

Business name: Tenant diagnostics production vault  
Owning group: Reliability Diagnostics  
Environment: production  
Primary owner: Nia Grange, `nia.grange@northstar.example`  
Backup owner: Rafael Okafor, `rafael.okafor@northstar.example`  
Data steward: Maren Quill, `maren.quill@northstar.example`  
External access pattern: partner access is handled case-by-case with project
owner and data-steward records attached to the ticket.
Notes: Support may open and route customer escalation tickets. Support ticket
ownership does not change the diagnostics project owner.

## `sandbox-tools`

Business name: Developer tools sandbox project  
Owning group: Developer Tooling  
Environment: sandbox  
Primary owner: Lena Ortiz, `lena.ortiz@northstar.example`  
Backup owner: Pavel Singh, `pavel.singh@northstar.example`  
Typical access groups: `sandbox-tools-buildkite`, `devtools-sandbox-readers`  
Supported short-lived roles: `sandbox_flag_operator`, `sandbox_log_viewer`  
Notes: The sandbox project hosts preview flag checks and build pipeline tests.
The owner record explicitly allows short-lived sandbox flag roles for build
groups managed by Developer Tooling.
