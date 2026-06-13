# Handoff request

Create a batch-level intake summary for all CSV attachments in
`incoming/`. The review desk compares this packet with prior
monthly closeout packets, so start from the standard helper under
`scripts/` and keep the output field order unchanged.

The reviewer needs:

- per-attachment parsed totals
- declared vs parsed total status
- manual-review list
- source and output manifest
- one row for every staged CSV attachment
