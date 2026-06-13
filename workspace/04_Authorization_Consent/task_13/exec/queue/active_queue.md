# Active IAM Queue

Queue source: access desk intake merge  
Batch label: `iam-morning-2026-06-08`  
Generated from: ticket intake, project owner mailbox, release desk routing,
support escalation notes, and sandbox operations calendar.

| Request ID | Requester | Resource | Environment | Requested Role | Target Principal | Requested Duration | Intake Channel |
|---|---|---|---|---|---|---|---|
| IAM-1401 | Maya Shah | `orion-telemetry-stg` | staging | `deploy_operator` | `group:ship-observability-rotators` | 7 days | project owner mailbox |
| IAM-1402 | Evan Pike | `payments-prod` | production | `prod_admin` | `user:miles.drexler@evergreen-contractors.example` | 14 days | calendar escalation |
| IAM-1403 | Nora Lee | `billing-ledger-prod` service account | production | `serviceAccountTokenCreator` | `group:billing-release-coordinators` | 48 hours | release desk thread |
| IAM-1404 | Priya Nandan | `tenant-diagnostics-prod` | production | `diagnostic_export_viewer` | `group:evergreen-sre-partner` | 30 days | support ticket comment |
| IAM-1405 | Lena Ortiz | `sandbox-tools` | sandbox | `sandbox_flag_operator` | `group:sandbox-tools-buildkite` | 10 days | sandbox operations calendar |

Intake summary:

- IAM-1401 is tied to the staging telemetry project used by the shipping
  observability rotation. The request references a short-lived deployment role
  and a standing on-call group.
- IAM-1402 concerns a production payments project. The requester is connected
  to checkout-web operations, while the target principal is a contractor
  working with the checkout stabilization group.
- IAM-1403 concerns a production billing service account. The release desk
  provided time pressure because a migration rehearsal is scheduled this week.
- IAM-1404 concerns a production diagnostics project and an external partner
  group supporting an incident reproduction effort.
- IAM-1405 concerns a sandbox project owned by the developer-tools group and a
  short-lived buildkite group used for preview flag maintenance.
