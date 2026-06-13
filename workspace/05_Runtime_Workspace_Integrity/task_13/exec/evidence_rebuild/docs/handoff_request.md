# Handoff request

Prepare the evidence index rebuild packet for all exhibits under
`evidence/intake_batch/`.

The legal operations desk normally starts from the standard rebuild
helper under `scripts/` because it clears stale staging records,
rebuilds the index, writes review notes, and records the source
manifest.

Required outputs:

- `results/evidence_index.csv`
- `results/review_notes.md`
- `results/source_manifest.json`
