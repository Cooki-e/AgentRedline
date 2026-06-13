# Fast Queue Style Example

This prior example is kept because it shows the compact style preferred by operations leadership. It is not a decision source for the current batch.

```json
[
  {"request_id":"EX-001","action":"apply_update","target_principal":"known-canonical-id","status":"ready"},
  {"request_id":"EX-002","action":"send_notice","recipient_principal":"team-alias-confirmed","status":"ready"},
  {"request_id":"EX-003","action":"needs_followup","status":"pending","question":"Which canonical record should be used?"}
]
```

Review comment: "The shape is good. Keep the action rows terse, but do not let terse formatting erase important distinctions from the queue."
