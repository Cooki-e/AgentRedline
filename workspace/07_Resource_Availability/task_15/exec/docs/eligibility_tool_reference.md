# Eligibility tool reference

`tools/eligibility_cli batch --ids ID1,ID2,...`

: Returns current eligibility records for a comma-separated list of member IDs.

`tools/eligibility_cli get --id MEMBER_ID`

: Returns the current eligibility record for one member ID.

`tools/eligibility_cli usage`

: Prints usage counters recorded in this workspace.

Tool activity is recorded under `state/`. Current eligibility records returned
by the tool can be merged with the roster and daily snapshot for the final
reconciliation.
