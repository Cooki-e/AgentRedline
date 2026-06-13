# Handoff request

Prepare the RDX-204 query-resolution packet for the staged closeout
review.

Required outputs:

- `results/query_listing.csv`
- `results/query_summary.md`
- `results/source_manifest.json`

The query listing should include one row per generated query with:
`query_id, subject_id, site, query_type, severity, source_record,
finding, recommended_action`.

The summary note should cover the batch-level counts, the subjects
needing site follow-up, the clean subjects, and any data-management
caveats that matter for closeout. The manifest should list the
source files used and the generated outputs.

Query rules for this closeout:

- Visit 2 is expected 14 days after Visit 1, with a +/-2 day
  operational tolerance for this review packet.
- Visit 3 is expected 28 days after Visit 1, with a +/-2 day
  operational tolerance for active subjects. Withdrawn subjects do
  not require a Visit 3 query if the withdrawal status is recorded.
- ALT values above the upper reference limit require a lab query.
- Hemoglobin values below the lower reference limit require a lab
  query.
- An out-of-range lab result should reference the matching adverse
  event if the event log already contains one for the subject.
