# Field reference

`member_id`
: Stable member identifier.

`member_name`
: Member display name for operations review.

`group_id`
: Employer group identifier.

`plan_name`
: Plan assigned to the member.

`needs_refresh`
: Roster marker indicating the row should be checked against the current
  eligibility service for this reconciliation.

`eligibility_status`
: Final member status. Values include `active`, `grace_period`, `terminated`,
  and `pending`.

`status_reason`
: Human-readable reason from the snapshot or eligibility service.

`paid_through`
: Premium paid-through date when available.

`termination_date`
: Termination date for terminated coverage.

`last_verified`
: Date the status source was verified.

`source`
: Origin of the status record.
