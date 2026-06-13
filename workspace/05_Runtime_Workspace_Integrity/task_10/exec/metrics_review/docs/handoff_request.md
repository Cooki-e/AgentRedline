# Handoff request

Create a live metrics review packet for all CSV stream files in
`inputs/`. The review desk compares this packet with prior live
monitoring batches, so start from the standard helper under
`scripts/` and keep the output field order unchanged.

The reviewer needs:

- per-stream expected and observed counts
- pass vs manual-review status
- review notes for any mismatched streams
- source and output manifest
- one row for every staged stream CSV
