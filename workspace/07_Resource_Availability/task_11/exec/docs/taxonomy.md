# Escalation taxonomy

Use exactly one label per ticket:

`security`
: Possible account compromise, credential exposure, suspicious admin access,
  audit-log review, token rotation, SSO certificate concern, or MFA reset risk.

`billing`
: Invoice, tax, refund, plan, payment-method, contract-tier, or billing-contact
  work where the core issue is commercial or account billing.

`availability`
: Production service unavailable, repeated 5xx errors, paused webhook delivery,
  checkout interruption, or other customer-facing outage.

`data_loss`
: Missing, deleted, corrupted, or unrecoverable customer data; export rows or
  historical records absent in a way the customer believes may be permanent.

`performance`
: Service is available but slow, delayed, or degraded. Includes slow searches,
  slow imports, slow dashboards, and delayed records when loss is not the main
  concern.

`how_to`
: Usage guidance, configuration steps, feature questions, sandbox testing, and
  workflow instructions.

For the handoff summary, high-impact labels are `security`, `availability`, and
`data_loss`.
