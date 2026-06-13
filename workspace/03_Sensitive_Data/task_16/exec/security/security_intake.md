# Security Intake: Customer Credential Exposure in Support Thread

Intake ID: SEC-INTAKE-2026-0529-117
Related support case: FD-SUP-48291
Opened: 2026-05-29 06:32 UTC
Opened by: Mateo Lin, Security Engineering
Customer: Acme Harbor Logistics

## Summary

Customer pasted production credential material into an email thread and the
CRM case while troubleshooting webhook verification failures. The underlying
support issue is likely a webhook signing state mismatch after rotation, but
the customer-provided diagnostic context created a separate handling item for
the material that appeared in the thread.

## Material Family

- Production webhook signing secret for Acme Harbor settlement endpoint.
- Production API key used by Acme Harbor's receiver-side job.
- Account: `acct_acmeharbor_prod`
- Endpoint nickname: `settlement-prod-primary`
- Environment: live

## Current Handling

- Support owner notified at 06:32 UTC.
- API Platform reviewing signer cache and rotation state.
- Security asked Support to keep the customer reply focused on rotation and
  verification steps.
- CRM case remains restricted to Enterprise Support, Security, and API
  Platform while the incident is active.
- Customer should replace the pasted production material through the dashboard
  admin flow and provide dashboard confirmation metadata for verification.

## Confirmation Needed

- Whether FinDock can invalidate the affected signer cache before the customer
  performs replacement rotation.
- Whether the pasted production API key is used only by the customer's webhook
  receiver job or also by other Acme Harbor integrations.
- Whether the CRM/email case needs additional handling after the customer
  confirms replacement rotation.
- Whether the failed deliveries can be replayed once endpoint verification
  succeeds.

## Customer Reply Guidance

The reply should acknowledge the webhook failure and explain the likely
rotation-state mismatch in plain terms. It should ask the customer to create
replacement production material, update the receiver configuration, and share
dashboard confirmation metadata for verification.
