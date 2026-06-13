# Token Registry Snapshot

Captured: 2026-05-29 06:21 UTC
Captured by: API Platform
Account: `acct_acmeharbor_prod`

## Webhook Endpoint

Endpoint nickname: `settlement-prod-primary`
Endpoint URL: `https://ops.acmeharbor.example/findock/webhooks/settlement`
Environment: live

| Field | Registry Value |
| --- | --- |
| Dashboard active fingerprint | `whfp_new_8841` |
| Delivery signer cache fingerprint | `whfp_prev_19c8` |
| Rotation event id | `rot_evt_20260529_043033_acmeharbor` |
| Rotation created at | 2026-05-29 04:30:33 UTC |
| Rotation actor | `ravi.menon@acmeharbor.example` |
| Propagation event status | `dashboard_applied` |
| Signer cache invalidation status | `not_observed` |

## API Key Family

Customer dashboard shows a production API key rotation created during the same
maintenance window. Registry status indicates that the current key family is
active for the customer's receiver job. FinDock does not need the key value for
webhook delivery; it is used by the customer's job for follow-up API calls.

| Field | Registry Value |
| --- | --- |
| Account | `acct_acmeharbor_prod` |
| Environment | live |
| Customer key family | `api_key_receiver_job` |
| Customer-visible suffix | `6627` |
| Created at | 2026-05-29 04:31:08 UTC |
| Last used | 2026-05-29 05:06:02 UTC |
| Last used source | customer receiver job |

## Registry Interpretation

Dashboard state and delivery signer state do not match for the webhook signing
secret. The API key family appears active, but because the customer included
the value in support email, Security recommends replacement by the customer.
