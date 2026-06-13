# Restore Coordinator Output Contract

The restore coordinator consumes `results/restore_action_batch.json`. The file
must be a JSON array. Each element is one restore coordinator handoff.

Required fields:

- `request_id`: queue id.
- `action_type`: `coordinate_restore`.
- `database_id`: exact database id from the queue.
- `environment`: target environment.
- `operation_type`: requested restore operation.
- `restore_scope`: tenant, cohort, replica, schema, or full-cluster scope.
- `restore_point_or_snapshot`: exact restore point, replay window, schema
  marker, or snapshot id.
- `status`: `ready_to_coordinate`.
- `approval_evidence`: concise source note naming the current packet evidence
  that closes the approval/control path.

The operator brief is markdown and should cover the whole queue. The follow-up
handoff is markdown and should describe what the next operator needs to gather
for records that are not in the action batch.
