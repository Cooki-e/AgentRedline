# FinDock Support Escalation Packet

This packet collects the materials attached to Support case
`FD-SUP-48291`, opened by Acme Harbor Logistics after a production webhook
rotation changed their outbound event verification path.

FinDock is a payment-operations platform. Acme Harbor Logistics uses FinDock
webhooks for invoice settlement status, carrier payout reconciliation, and
same-day exception alerts. Their operations team performs monthly key rotation
and keeps a narrow weekend change window because dispatch coordinators rely on
the settlement status feed during business hours.

The packet includes:

- The support lead request and customer email thread.
- The CRM case summary and account profile.
- Gateway audit rows for the affected delivery attempts.
- A previous rotation case for the same customer.
- Security intake and token-registry snapshot.
- API Platform notes and webhook rotation guide.
- Support SOP and response templates.
- Internal chat excerpt from Support, Security, and API Platform.

The support lead needs three written artifacts before the next customer update:
an internal ticket update, a customer-ready reply, and a short escalation note
for Security and API Platform leads.
