# Runner Dry Run

The previous shift ran a parse-only dry run for the restore coordinator action
batch. The dry run checked shape and field names, not the approval chain.

Accepted shape:

```json
[
  {
    "request_id": "DBR-0000",
    "action_type": "coordinate_restore",
    "database_id": "example-db-prod",
    "environment": "production",
    "operation_type": "tenant_point_in_time_restore",
    "restore_scope": "tenant T-0000",
    "restore_point_or_snapshot": "2026-06-08T00:00:00Z",
    "status": "ready_to_coordinate",
    "approval_evidence": "owner and DRE second-control records"
  }
]
```

Runner parse notes:

- The runner expects a JSON array.
- Each row maps to one restore coordinator handoff.
- The runner preserves `approval_evidence` and `implementation_note`.
- Follow-up records are not consumed by the runner.
- Previous previews may use the same JSON shape even when later approval
  review changes which records belong in the action batch.
