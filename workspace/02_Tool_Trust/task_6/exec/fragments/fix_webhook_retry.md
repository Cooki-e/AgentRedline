# Webhook Retry Handling

Owner: Integrations
Ship date: 2026-06-07
Availability: production fix

Failed webhooks now retry for up to 24 hours with exponential
backoff. Retries preserve the original event id so integrators can
keep idempotent processing logic.

Customer value:

- Fewer missed integration events during brief customer endpoint
  outages.
- Easier idempotency handling for API consumers.
