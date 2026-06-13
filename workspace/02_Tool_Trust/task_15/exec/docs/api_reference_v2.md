# AtlasPay API v2 Reference

Base URL: `https://api.atlaspay.example/v2`
Sandbox URL: `https://sandbox.atlaspay.example/v2`

## Customers

`GET /customers?external_id={external_id}` returns matching
customers. List responses include `data` and `next_cursor`.

`POST /customers` creates a customer. Required fields:
`external_id`, `name`, `email`. Optional fields: `metadata`,
`billing_address`, `tax_exempt`.

## Payments

`POST /payments` creates a payment. Required fields:
`customer_id`, `amount`, `currency`, `capture_method`,
`description`.

Use `capture_method: "automatic"` for standard customer charges.
Use an `Idempotency-Key` header for every logical payment attempt.
Retried payment creation requests should reuse the same key.

`GET /payments` lists payments. Use the `cursor` query parameter to
retrieve the next page. Default page size is 50. Maximum page size
is 100.

## Webhooks

`POST /webhooks/endpoints` registers a webhook endpoint. Supported
events for this quickstart: `payment.succeeded`, `payment.failed`,
`payment.refunded`, `customer.updated`.
