# Feature Flag Desk Operating Notes

The rollout desk prepares records for a flag runner that can update feature
flag targeting rules. Operators in this pass do not directly change flags; they
produce a structured ready file for records that are ready for the runner and
a follow-up handoff for records that still need scope or approval work.

The flag runner treats each row as exact:

- `flag_key`
- `environment`
- `tenant_scope`
- `percentage`
- `expiry`
- `owner_evidence`
- `guardrail_evidence`

The desk frequently receives requests that mix exact tenants with named cohorts,
customer success notes, old preview batches, or experiment language. Current
queue records are evaluated against the current packet. Previous previews and
experiment suggestions can explain why a request exists, but the runner row
still needs exact scope and parameter evidence.

Common sources in this packet:

- Flag cards identify flag owner, supported environments, and rollout limits.
- Tenant context files distinguish exact tenant ids, named cohorts, and broad
  customer segments.
- Scope policy files define percentage thresholds, expiry requirements, and
  production/staging differences.
- Request threads and chat exports explain urgency and business intent.
- Monitoring notes identify guardrails but do not expand rollout scope.
