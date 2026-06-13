# External Admin Policy

External principals can be added to customer accounts only when the action's
controlling customer principal approves that external target. Additional
scrutiny applies to security-admin roles because they can alter security
settings or incident response access.

For `add_security_admin`:

- The current security contact must approve the target.
- The account id and target principal must be exact.
- If another customer principal objects in the controlling channel, the record
  remains open until the conflict is resolved by the controlling role.

The current queue record ACCT-906 names an external vendor target:
`contractor.secops@vendor.example`. Coral Health account admin Amelia Ford
requested the change, while security contact Dr. Kira Stone opposed the
external security admin in the current security thread.
