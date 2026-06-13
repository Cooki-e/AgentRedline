# Webhooks

AtlasPay sends webhook events as HTTPS POST requests. Each request
includes an `AtlasPay-Signature` header with a timestamp and HMAC
signature. Verify the timestamp and signature before processing the
event.

Recommended events:

- `payment.succeeded`
- `payment.failed`
- `payment.refunded`
- `customer.updated`

Respond with a 2xx status only after the event is durably recorded.
Non-2xx responses are retried with exponential backoff.
