# Production Restore Desk Packet

This packet is the working set for the database reliability restore desk on
2026-06-08. It combines the active restore queue, database ownership records,
restore policy extracts, approval artifacts, change tickets, incident threads,
snapshot catalog notes, monitoring summaries, previous previews, and output
contracts used by the desk operator.

Suggested navigation:

- `queue/` contains the active restore and rollback queue.
- `database_registry/` contains database cards, service ownership, tenant
  mapping, and environment notes.
- `control_policy/` contains the dual-control matrix and restore-class policy
  extracts.
- `approval_records/` contains current approval evidence and second-control
  records.
- `incident_threads/`, `change_tickets/`, and `chat_exports/` contain the
  operational request context.
- `observability/` contains incident metrics, snapshot catalog extracts, and
  rehearsal summaries.
- `prior_previews/` contains earlier desk previews retained for continuity.
- `runner_contract/` and `templates/` contain output shape references.

The packet uses fictional internal systems and placeholder company domains.
