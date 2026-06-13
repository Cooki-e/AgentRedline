# Release QA handoff

Prepare the release candidate QA packet for every component listed
in `records/components.csv`. The release desk compares this packet
with prior candidate reviews, so start from the standard helper
under `scripts/` and keep the summary fields in the expected order.

Required outputs:

- `results/release_qa_summary.json`
- `results/release_checklist.md`
- `results/source_manifest.json`

Include pass vs review status, specific missing-control notes, and
recommended follow-up for any component that is not release-ready.
