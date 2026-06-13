# Action Scope Rules

The runner expects exact account and action scope. Role-specific authority must
match the action:

- An account admin approval for `add_account_admin` does not approve
  `add_security_admin`.
- A billing owner approval for `transfer_billing_owner` does not approve MFA,
  SSO, or account admin changes.
- An invoice contact approval for `add_invoice_recipient` does not approve
  billing owner transfer or account admin membership.
- A support owner can open a support workspace task but does not become the
  customer's SSO contact.
- A CSM can represent urgency and business impact but does not control account
  security policy.

When customer principals conflict for an action, the desk keeps the record out
of the ready file and routes it to follow-up for the controlling principal.
