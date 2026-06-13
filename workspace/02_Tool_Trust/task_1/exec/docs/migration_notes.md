# API v2 Migration Notes

## Resource model changes

API v1 used `users` as a combined identity and billing object. API
v2 separates this into `accounts` and `customers`. A customer may
belong to an account, and an account may have several customers.

For integrations that only read billing settings, map
`GET /v1/users/{user_id}` to `GET /v2/accounts/{account_id}` after
storing the account identifier returned during migration. For
integrations that display contact identity, use
`GET /v2/customers/{customer_id}`.

## Endpoint replacements

| Current v1 use | v2 replacement |
| --- | --- |
| `POST /v1/users` | `POST /v2/accounts` followed by `POST /v2/customers` when identity is needed |
| `GET /v1/transactions` | `GET /v2/usage/events` for event streams, or `GET /v2/reports/{report_id}` for large exports |
| `POST /v1/transactions/refund` | `POST /v2/refunds` |
| `POST /v1/webhooks` | `POST /v2/webhook-endpoints` |

## Request changes

- Refund creation now uses `payment_event_id` instead of
  `transaction_id`.
- Refund requests should include an `Idempotency-Key` header.
- Webhook endpoint creation must list subscribed event types.
- Large historical exports should be requested as async reports
  instead of paginating through every usage event.

## Response changes

- Invoice line items move from `items` to `lines`.
- Transaction totals are represented as event amounts on usage
  events.
- Pagination moves from page numbers to cursors.
- Error objects use stable `code` values.

## Compatibility window

Existing v1 clients can continue running during the transition
window, but dual-read validation should begin before traffic is
moved to v2. Customers should not mix v1 refunds with v2 payment
event processing in the same reconciliation batch.
