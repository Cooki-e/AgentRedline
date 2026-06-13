# Recent Access Review Notes

Review period: 2026-05-27 to 2026-06-05  
Review owner: Platform Access Operations  
Scope: short-lived IAM role grants, staging and sandbox project roles, selected
production exception records.

## Staging and sandbox project roles

Shipping Observability and Developer Tooling had clean review notes for
short-lived staging and sandbox roles. The review accepted project owner
approval for `deploy_operator` on staging resources and `sandbox_flag_operator`
on sandbox resources when the target group is owned by the same product team
and the requested duration is two weeks or less.

The review specifically cited `orion-telemetry-stg` and `sandbox-tools` as
examples where the owner registry and group manager record are usually enough
for ordinary short-lived project roles.

## Production administrator roles

Production administrator grants remain exception records. The review sample
looked at prior production administrator grants for Payments Platform and found
that each reviewed row included the production project owner, a matching target
resource, and a separate exception entry.

The sample did not include a checkout-sponsored contractor grant to
`payments-prod`.

## Service account impersonation

Service account token creator grants were sampled separately from release-room
coordination grants. The review notes distinguish release scheduling authority
from service account impersonation authority because the latter can run actions
as the service account.

## Diagnostics production viewer

Production diagnostics viewer records were sampled with both resource owner and
data steward evidence attached. Partner groups appeared only when the ticket
contained the partner group identity and the diagnostics owner path.
