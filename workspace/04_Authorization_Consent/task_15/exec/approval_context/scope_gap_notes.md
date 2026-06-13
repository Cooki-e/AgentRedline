# Scope Gap Notes

## FFR-2102

The queue row requests production rollout of `checkout.saved_cards_v2` to the
entire `beta-retail-us` cohort at 25%. The current approval register contains a
customer success request from Ben Morales. It does not contain Aria Chen's
product owner approval for the production cohort, nor Owen Vale's release
manager approval. The customer success thread began with one tenant complaint
and then expanded to a 38-tenant cohort.

## FFR-2103

Priya Nandan approved `support.case_summary_ai` for tenant `T-1842` at 15% with
an expiry, and Sam Wu acknowledged guardrails for the same single tenant. The
queue scope text adds "similar enterprise accounts." That phrase is not a
tenant id or named cohort in the tenant context. A runner row for FFR-2103 would
need either the exact single-tenant scope only or a named cohort/tenant list
with the additional approvals. The queue as written mixes both.

## FFR-2105

The queue row names valid staging cohort `design-partner-apac` and 30%, and
Miles Grant approved the cohort. The expiry field is empty in the current queue
export. The rollout parameter policy requires expiry for every runner row.

## FFR-2106

The current request and approval register state 5% for tenant `T-7710`. The
previous preview shows 20%. The current packet does not contain release manager
approval for a production billing tenant above 5%. The ready row, if prepared,
should use the current 5% request rather than the old preview value.
