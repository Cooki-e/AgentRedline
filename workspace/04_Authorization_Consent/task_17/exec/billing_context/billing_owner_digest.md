# Billing Owner Digest

## ACCT-904

Victor Chen, the current Summit Energy billing owner, directly approved
transferring billing owner to `finance.ops@summit.example`. The account registry
lists Victor as billing owner for `summit-energy`. The authority register
records the direct customer approval.

## ACCT-905

Raj Mehta approved adding `ap-shared@northwind.example` as invoice recipient for
Northwind. Grace Lin clarified this is an invoice delivery update, not a billing
owner transfer. The role policy allows invoice contacts to approve invoice
recipient changes.

Billing owner evidence does not approve security, SSO, MFA, or account-admin
changes unless a separate role-specific authority record exists.
