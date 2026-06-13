# Flag Runner Output Contract

The flag runner consumes `results/ready_rollouts.json`. The file must be a JSON
array. Each element represents one feature flag rollout that is ready to apply.

Required fields:

- `request_id`: queue id.
- `action_type`: `set_feature_flag_rollout`.
- `flag_key`: exact flag key.
- `environment`: exact environment.
- `target_scope`: exact tenant id or named cohort.
- `percentage`: numeric rollout percentage.
- `expiry`: expiry timestamp.
- `status`: `ready_to_apply`.
- `scope_evidence`: concise source note showing why the scope and parameter
  values are ready from the current packet.
- `guardrail_evidence`: concise source note for guardrails, where applicable.

Records that still need scope clarification, expiry, approval, or parameter
correction are handled in the brief and follow-up handoff.
