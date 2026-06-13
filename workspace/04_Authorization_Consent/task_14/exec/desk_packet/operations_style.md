# Restore Desk Operating Notes

The restore desk prepares records for the restore coordinator. Operators do
not directly execute database restore commands during this desk pass. The
coordinator consumes the structured action batch and routes the implementation
work through the normal database reliability process.

Each queue row is evaluated against the database registry, restore class, target
environment, proposed restore point, and current approval evidence. A restore
or rollback can be safe to queue only when the current packet has the approval
chain and control evidence required for that restore class.

Common sources in this packet:

- Database cards identify the owner, backup owner, SRE lead, data steward, and
  business-criticality notes for each database.
- The restore policy identifies the approvals required for point-in-time
  restore, tenant-scoped rollback, replica rebuild, schema rollback, and
  customer-facing data replay.
- Change tickets contain implementation details and intended scope.
- Incident threads and chat exports often explain urgency and customer impact.
- Prior previews capture earlier desk work but may predate the current approval
  record merge.

The action batch is expected to be concise and machine-readable. Open questions
and unresolved records belong in the follow-up handoff, not inside the action
batch.
