# AtlasPay API v1 Reference

API v1 is still available for existing customer integrations until
the end of the transition window. New customer integrations should
use API v2.

## Core endpoints

| v1 endpoint | Purpose | Notes |
| --- | --- | --- |
| `GET /v1/users/{user_id}` | Retrieve a user profile tied to a billing account. | User records combine identity and account settings. |
| `POST /v1/users` | Create a user and default billing account. | Creates a user and account in one request. |
| `GET /v1/transactions` | List transaction records. | Offset pagination with `page` and `per_page`. |
| `POST /v1/transactions/refund` | Create a refund for a settled transaction. | Uses `transaction_id` in the JSON body. |
| `GET /v1/invoices/{invoice_id}` | Retrieve an invoice. | Response embeds line items under `items`. |
| `POST /v1/webhooks` | Register a webhook endpoint. | Uses shared secret signatures. |

## Authentication

API v1 accepts a static API key in the `X-Atlas-Key` header. Keys
are scoped to the merchant account and rotate manually through the
dashboard.

## Response shape

Most v1 list endpoints return:

```json
{
  "data": [],
  "page": 1,
  "per_page": 50,
  "total": 123
}
```

## Error shape

Errors use the fields `error`, `message`, and `request_id`.
