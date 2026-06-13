# Rollout Parameter Policy

The feature flag runner requires exact parameters for every ready row:

- flag key
- environment
- tenant id or named cohort
- rollout percentage
- expiry timestamp
- owner or approval evidence
- guardrail evidence

## Exact tenant scope

An exact tenant rollout uses a single tenant id such as `tenant:T-0427`.
Adjacent customer notes, similar-account phrases, or broad segment labels do
not extend the runner row.

## Named cohort scope

A named cohort rollout uses a cohort key from `tenant_context/cohort_definitions.md`.
Production cohort rollout requires the approvals listed in the threshold
policy. Staging cohort rollout still requires expiry.

## Percentage

The runner uses the current queue percentage unless an approval record
explicitly changes it. Previous previews are not parameter updates. Production
percentages above the threshold require the matching release approval.

## Expiry

Every rollout row needs an expiry timestamp. Empty expiry fields stay out of
the ready file until the requester or owner supplies the expiry.

## Environment

The environment field is exact. Sandbox, staging, and production records should
not be merged or substituted.
