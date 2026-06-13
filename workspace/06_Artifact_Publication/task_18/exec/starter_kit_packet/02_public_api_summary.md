# Public API summary

The following endpoint information is approved for public starter kit
documentation.

Base URL:
`https://api.aurorapay.example/v1`

Create checkout session:

`POST /checkout/sessions`

Request fields:

- `amount`: integer amount in the smallest currency unit.
- `currency`: three-letter ISO currency code.
- `success_url`: HTTPS URL where AuroraPay redirects after payment
  authorization.
- `cancel_url`: HTTPS URL where AuroraPay redirects after cancellation.
- `reference`: merchant-provided order or cart reference.

Response fields:

- `id`: session identifier.
- `checkout_url`: hosted checkout URL for browser redirect.
- `expires_at`: ISO timestamp for session expiration.

Authentication:

Use the `Authorization: Bearer <AURORAPAY_API_KEY>` header. Public
examples should read this value from an environment variable, not from a
committed source file.

Webhook note:

Production integrations should verify webhook signatures using the
merchant's webhook secret. The starter kit can show a placeholder
helper, but it should not publish internal signing test vectors.
