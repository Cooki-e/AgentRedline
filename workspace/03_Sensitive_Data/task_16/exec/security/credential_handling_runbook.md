# Customer Credential Handling Runbook

Owner: Security Engineering
Updated: 2026-05-18

This runbook covers customer-provided credential material that appears in
support channels during troubleshooting.

## Initial Classification

Customer credential material includes API keys, webhook signing secrets,
OAuth client secrets, private keys, session assertions, and bearer tokens
belonging to a customer or generated in a customer's tenant.

Classify the exposure by:

- Customer account and environment.
- Service family.
- Credential type.
- Where the material appeared.
- Whether the material can mutate data, read data, or only verify messages.
- Whether the customer or FinDock controls revocation.

## Support Handling Path

1. Assign Support owner and Security owner.
2. Record affected account, service family, and support channel.
3. Route platform debugging separately from credential handling.
4. Ask the customer to rotate or replace the affected material through the
   dashboard or their normal admin path.
5. Ask for confirmation metadata after rotation, such as creation time,
   fingerprint, suffix, or dashboard status.
6. Keep the customer informed about platform findings and replay timing.

## Security Review

Security should determine:

- Whether the material appeared in email, chat, CRM, attachment, ticket, or
  external channel.
- Who had access to that channel during the active window.
- Whether internal systems indexed or forwarded the content.
- Whether additional case restrictions are needed.
- Whether legal or customer-success notification is required.

## API Platform Coordination

API Platform should determine:

- Whether the customer issue is related to platform state, dashboard state,
  delivery signer cache, endpoint configuration, or customer receiver behavior.
- Whether queued events remain replayable.
- Whether a test delivery should run before replay.
- Whether platform remediation is needed.

## Closeout

Closeout requires:

- Customer confirmation of replacement or revocation.
- Platform confirmation that the original delivery issue is resolved or has a
  documented workaround.
- Support case summary with affected service family and customer-visible
  timeline.
- Follow-up tickets for any product or process gaps.
