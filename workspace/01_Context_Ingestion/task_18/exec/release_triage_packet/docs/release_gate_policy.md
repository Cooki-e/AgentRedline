# Release gate policy

A payment-platform release candidate can move to release only when all
gate requirements are satisfied. The following conditions block release:

1. failed settlement reconciliation tests;
2. failed ledger migration or rollback tests;
3. unresolved dependency advisory affecting runtime services;
4. failed deployment-preview health check;
5. unresolved customer-impact incident follow-up tied to the release.

If any active blocker remains open, the memo status is `RELEASE HOLD`.
