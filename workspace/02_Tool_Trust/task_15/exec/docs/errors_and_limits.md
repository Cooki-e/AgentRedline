# Errors and Rate Limits

Error responses include `error.code`, `error.message`, and
`request_id`.

Common codes:

- `400 invalid_request`
- `401 token_expired`
- `403 insufficient_scope`
- `404 not_found`
- `409 idempotency_conflict`
- `422 validation_failed`
- `429 rate_limited`

Default tenant rate limit: 600 requests per minute. Use exponential
backoff for `429` and `5xx` responses. For payment creation retries,
reuse the same `Idempotency-Key`.
