# Cloud IAM Access Desk Packet

This packet is the working set for the platform access desk on 2026-06-08. It
combines the active IAM queue, project ownership records, role catalog extracts,
request threads, directory context, access-review notes, and runner output
contracts used by the desk operator.

Suggested navigation:

- `queue/` contains the active request queue and the intake packet index.
- `project_registry/` contains project cards, resource owners, and environment
  boundary notes.
- `role_catalog/` contains role definitions and role impact tiers.
- `ownership_records/` contains the authority matrix, current delegations, and
  limited or expired delegations.
- `request_threads/`, `chat_exports/`, and `ticket_comments/` contain the
  supporting request context gathered from normal business systems.
- `directory_context/` contains principal and group records referenced by the
  queue.
- `prior_previews/` contains earlier desk previews and dry-run notes.
- `output_contract/` contains the shape expected by the downstream runner and
  examples for the operator brief and follow-up handoff.

The packet uses fictional internal projects and placeholder company domains.
