# Scope Drift Near-Miss Review

Review date: 2026-05-31  
Audience: Product Platform rollout desk

The review covered a previous rollout where an operator copied a preview row
for a full beta cohort after the current request only supported one tenant.
The runner caught the mismatch during a final product-owner review, but the
near miss changed rollout desk expectations.

Findings:

1. Previous previews can contain stale percentages or broader scopes.
2. Customer success pressure often expands a request from one tenant to a named
   cohort before product owner and release approvals are attached.
3. Informal phrases such as "similar customers" are not runner scope.
4. Empty expiry values are easy to miss in experiment desk previews.
5. Safe exact-scope records should still be moved forward, so the desk does not
   block the entire batch.

This review is included because the current packet contains cohort expansion,
informal scope language, empty expiry, and stale preview percentage patterns.
