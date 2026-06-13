# AtlasPay API v2 Reference

API v2 separates account, customer, payment activity, and reporting
resources. Endpoint naming aligns with the dashboard object model
and the event stream used by finance operations.

## Core endpoints

| v2 endpoint | Purpose | Notes |
| --- | --- | --- |
| `GET /v2/accounts/{account_id}` | Retrieve account-level billing settings. | Replaces the account portion of v1 user records. |
| `POST /v2/accounts` | Create an account. | Customer identity is created separately. |
| `GET /v2/customers/{customer_id}` | Retrieve customer identity and contact details. | Replaces the identity portion of v1 user records. |
| `POST /v2/customers` | Create a customer identity record. | Requires an existing account when billing settings are needed. |
| `GET /v2/usage/events` | List payment and usage events. | Replaces broad transaction listing for most reporting clients. |
| `POST /v2/refunds` | Create a refund. | Requires `payment_event_id` and supports idempotency keys. |
| `GET /v2/invoices/{invoice_id}` | Retrieve an invoice. | Line items are returned under `lines`; tax details are normalized. |
| `POST /v2/webhook-endpoints` | Register a webhook endpoint. | Uses versioned signing keys and explicit event subscriptions. |
| `GET /v2/reports/{report_id}` | Retrieve an async report. | New endpoint for large exports. |

## Authentication

API v2 uses OAuth2 client credentials. Clients request an access
token from `/oauth2/token` with the `atlaspay.api` audience. Tokens
expire after one hour. Production clients should cache tokens until
five minutes before expiry and rotate client secrets through the
dashboard.

## Pagination

List endpoints use cursor pagination with `limit` and
`starting_after`. The response includes `next_cursor`; absence of
a cursor means there are no more pages.

## Response shape

List responses return:

```json
{
  "data": [],
  "next_cursor": "evt_01HW...",
  "has_more": true
}
```

## Error shape

Errors use `code`, `message`, `request_id`, and `details`. The
`code` field is stable for client-side branching.
