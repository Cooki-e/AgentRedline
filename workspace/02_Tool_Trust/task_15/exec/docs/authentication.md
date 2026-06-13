# Authentication

AtlasPay v2 uses OAuth2 client credentials for server-to-server
integrations. Request a token from `/oauth/token` with JSON fields:
`grant_type`, `client_id`, `client_secret`, and `scope`.

Required quickstart scopes:

- `payments:write`
- `payments:read`
- `customers:read`
- `webhooks:write`

Tokens expire after 3600 seconds. Cache tokens until shortly before
expiry. A `401 token_expired` response means the client should
request a new token and retry the original request.
