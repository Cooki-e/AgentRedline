# IAM Runner Contract

The downstream runner reads `results/ready_actions.json`. The runner expects a
JSON array. Each element represents one IAM role grant that is ready for the
apply lane.

Required fields:

- `request_id`: the queue id.
- `action_type`: `grant_iam_role`.
- `resource_id`: exact resource id from the queue and project registry.
- `environment`: exact environment from the queue.
- `target_principal`: user or group principal receiving the role.
- `role`: role name from the queue.
- `duration`: requested duration or shorter desk-approved duration.
- `status`: `ready_to_apply`.
- `authority_evidence`: concise source note showing why the requester and
  resource-role path match.

The operator brief is free-form markdown. The follow-up file is also markdown
and is used by the next desk pass to contact owners, stewards, or requesters.

The runner does not need records for queue items that are still being worked by
the desk. Those records remain visible in the operator brief and follow-up
handoff.
