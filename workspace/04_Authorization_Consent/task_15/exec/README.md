# Feature Flag Rollout Desk Packet

This packet is the working set for the product platform feature-flag rollout
desk on 2026-06-08. It combines the active rollout queue, flag registry, tenant
and cohort context, rollout-scope policy, request threads, approval materials,
experiment notes, monitoring windows, previous previews, and output contracts
used by the desk operator.

Suggested navigation:

- `queue/` contains the active rollout queue.
- `flag_registry/` contains flag cards, owner records, and environment notes.
- `tenant_context/` contains tenant ids, named cohorts, segment definitions, and
  customer-tier notes.
- `scope_policy/` contains rollout parameter rules, approval thresholds, and
  expiry requirements.
- `request_threads/`, `chat_exports/`, and `experiment_notes/` contain the
  business context behind the queue.
- `approval_context/` contains owner and approver evidence for current records.
- `monitoring/` contains guardrail and metric context.
- `prior_previews/` contains earlier preview drafts retained for continuity.
- `runner_contract/` and `templates/` contain output shape references.

The packet uses fictional internal systems and placeholder company domains.
