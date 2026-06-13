# Webhook Rotation Guide

Audience: Enterprise Support and API Platform
Updated: 2026-05-10

## Normal Rotation Flow

1. Customer creates a new signing secret in the dashboard.
2. Dashboard marks the new secret as pending.
3. Customer updates receiver configuration.
4. Customer sends a test delivery.
5. If the test succeeds, dashboard marks the new secret active.
6. Delivery signer cache receives the endpoint rotation event.
7. Queued events continue with the active signing secret.

## Dual-Secret Grace Period

Enterprise accounts can keep the previous signing secret valid for up to six
hours during planned rotation. During the grace period, customers may accept
both old and new signatures. Acme Harbor usually disables dual-secret grace
after the first successful test because their receiver library supports only
one active secret at a time.

## Failure Modes

Signature verification failures after rotation usually come from one of four
causes:

- Customer receiver was updated before the new secret became active.
- Customer receiver kept the previous secret after dashboard activation.
- Delivery signer cache kept the previous secret after dashboard activation.
- Customer endpoint changed validation logic or replay window settings.

## Support Diagnosis

Useful signals:

- Event ID and delivery ID.
- Endpoint nickname.
- Dashboard active fingerprint.
- Delivery signer cache fingerprint.
- Customer receiver fingerprint, if the customer can share it.
- Response status and reason.
- Whether control accounts are delivering normally.

The gateway audit should distinguish platform delivery failures from customer
receiver responses. A 401 from the customer receiver with healthy control
accounts usually points to endpoint-specific signature state rather than a
platform outage.

## Replay

Queued replay should wait for a successful test event. For enterprise payment
operations accounts, replay retention is 72 hours. API Platform can replay by
event type and time window.
