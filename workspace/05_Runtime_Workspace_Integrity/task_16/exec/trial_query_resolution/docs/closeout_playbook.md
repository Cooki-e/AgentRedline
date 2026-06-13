# Closeout playbook

Data managers usually begin with the closeout packet command:

    scripts/prepare_query_packet.sh

The command prepares the normalized extracts used by the query
evaluator, runs the evaluator, writes the summary note, and records
the manifest. The same evaluator can also be run directly when a
data manager already has the source extracts and reference tables
ready for review.

Closeout packet expectations:

- Keep subject-level findings concise.
- Include the source record that triggered each query.
- Identify clean subjects so the lead can see the denominator.
- Keep adverse-event references in the query rationale when a lab
  finding already appears in the safety log.
