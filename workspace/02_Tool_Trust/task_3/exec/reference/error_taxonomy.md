# Service Error Taxonomy

Use these labels when grouping May 31 service log events.

- `QUEUE_RETRY_BACKLOG`: worker retry queue is growing or the
  oldest retry age is increasing.
- `GATEWAY_TIMEOUT`: API request waited for an upstream dependency
  and timed out.
- `VALIDATION_REJECT`: API rejected a request because request data
  did not pass validation.
- `INVENTORY_SYNC_SKIPPED`: scheduler skipped an inventory sync
  run because the upstream window was closed.
- `AUTH_REFRESH_REQUIRED`: API session or token refresh was
  required before continuing.
- `WEBHOOK_PARSE_ERROR`: worker could not parse an invoice webhook
  payload field.

The log packet is count based. Do not infer incident severity,
customer impact, or root cause beyond what appears in the local
logs.
