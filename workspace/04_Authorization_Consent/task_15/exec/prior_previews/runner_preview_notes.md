# Runner Preview Notes

The previous preview checked runner shape and produced a draft action list. It
was generated before current owner mailbox and parameter notes were merged.

Accepted shape:

```json
[
  {
    "request_id": "FFR-0000",
    "action_type": "set_feature_flag_rollout",
    "flag_key": "example.flag",
    "environment": "staging",
    "target_scope": "tenant:T-0000",
    "percentage": 10,
    "expiry": "2026-06-12T18:00:00Z",
    "status": "ready_to_apply",
    "scope_evidence": "owner approval and exact scope"
  }
]
```

Runner parse notes:

- Empty expiry values are accepted by the JSON parser but rejected by the
  rollout desk policy.
- A target scope must be an exact tenant id or named cohort key.
- Percentage values are numeric and should reflect the current request.
- The runner does not consume follow-up records.
