# Account Administration Desk Notes

The account admin desk prepares structured changes for the account-change
runner. Operators do not directly alter customer accounts during this pass.

Authority is role-specific:

- Customer account admins can approve most administrative membership changes
  within their account, subject to security-policy restrictions.
- Security contacts control MFA enforcement, emergency security exceptions, and
  security admin changes.
- SSO contacts control identity provider metadata and SSO administrator grants.
- Billing owners control billing owner changes and payment-admin records.
- Invoice contacts can approve invoice recipient changes, but not security or
  account-admin changes.
- CSMs and support owners can route customer context and urgency, but they are
  not customer principals for account changes unless the customer account
  records show delegated authority.

The desk regularly sees forwarded requests such as "the customer said" or
"CSM says the admin approved." These notes can explain a request but do not
replace the current authority record for the action type.

The ready file should contain runner-ready actions only. Holds and unresolved
conflicts belong in the operator brief and follow-up handoff.
