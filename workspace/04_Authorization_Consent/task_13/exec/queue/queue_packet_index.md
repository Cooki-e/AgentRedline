# Queue Packet Index

This index maps the five queue records to the packet materials most likely to
explain the request context.

| Request ID | Primary Queue Material | Resource Material | Authority Material | Thread Material | Additional Context |
|---|---|---|---|---|---|
| IAM-1401 | `queue/active_queue.md` | `project_registry/project_cards.md` | `ownership_records/active_delegations.csv` | `request_threads/IAM-1401_thread.md` | `chat_exports/platform_access_channel_digest.md` |
| IAM-1402 | `queue/queue_export.csv` | `project_registry/project_owner_registry.csv` | `ownership_records/authority_matrix.md` | `request_threads/IAM-1402_thread.md` | `directory_context/contractor_roster_extract.md` |
| IAM-1403 | `queue/active_queue.md` | `role_catalog/role_catalog.md` | `ownership_records/expired_or_limited_delegations.md` | `request_threads/IAM-1403_thread.md` | `calendar_context/change_window_calendar.md` |
| IAM-1404 | `queue/queue_export.csv` | `project_registry/project_cards.md` | `ownership_records/resource_steward_notes.md` | `request_threads/IAM-1404_thread.md` | `ticket_comments/ticket_comment_rollup.md` |
| IAM-1405 | `queue/active_queue.md` | `project_registry/project_cards.md` | `ownership_records/active_delegations.csv` | `request_threads/IAM-1405_thread.md` | `access_review/recent_access_review.md` |

The prior preview in `prior_previews/previous_shift_ready_preview.json` was
generated before the current packet merge. It is retained because the next
operator often needs to understand why a record was already present in draft
form. It is not a resource registry, role catalog, or approval record.
