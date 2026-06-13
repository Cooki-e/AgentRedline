# AtlasPay v2 Release Notes

- v2 changes the base URL to `/v2`.
- OAuth2 client credentials replace static API keys for server
  integrations.
- Payment creation requires an idempotency key.
- Cursor pagination replaces page-number pagination.
- Webhook signatures use `AtlasPay-Signature`.
- Sandbox validation should cover token refresh, customer lookup,
  payment creation, pagination, webhook verification, and common
  error handling.
