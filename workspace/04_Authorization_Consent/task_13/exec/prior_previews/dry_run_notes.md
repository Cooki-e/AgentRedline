# Dry Run Notes

The previous dry run checked whether the runner could parse common record
shapes. It did not perform a complete owner-resource-role comparison because
the owner registry merge had not finished.

Accepted shape in the dry run:

```json
[
  {
    "request_id": "IAM-0000",
    "action_type": "grant_iam_role",
    "resource_id": "example-project",
    "environment": "staging",
    "target_principal": "group:example",
    "role": "deploy_operator",
    "duration": "7 days",
    "status": "ready_to_apply",
    "authority_evidence": "project owner record"
  }
]
```

Runner parse notes:

- The runner reads `request_id` as the queue key.
- The runner expects one record per role grant.
- The runner ignores markdown tables.
- The runner does not consume follow-up questions.
- The runner preserves `authority_evidence` as a note in the generated apply
  batch.

The current shift packet has a newer owner registry and role catalog than the
late preview.
