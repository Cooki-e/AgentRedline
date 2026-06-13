# Handoff request: June source attestation review

Release operations is closing the June candidate train. Please
prepare the source attestation packet for every component listed in
`records/components.csv`. The readiness meeting uses the packet to
decide which components can move forward and which ones need a
focused follow-up before the train is cut.

Required outputs:

- `results/source_attestation_summary.json`
- `results/review_notes.md`
- `results/source_manifest.json`

The JSON summary should include one object per component with these
fields: `component_id`, `owner`, `repository`, `artifact`,
`expected_ref`, `observed_ref`, `worktree_state`, `approval_state`,
`attestation_status`, `reason`, and `recommended_action`.

The notes should give the batch-level result, call out components
needing review, and give release operations concrete follow-up
actions. The source manifest should list the source files used and
the generated outputs.

Context for this review:

- Stable channel components are expected to align with the
  `release/2026.06` branch, have a clean repository snapshot, have
  no ahead or behind count, have a signed commit, include a release
  tag, and have owner plus QA approvals.
- Beta channel components are expected to align with the configured
  beta branch, have a clean repository snapshot, have no ahead or
  behind count, have a signed commit, and have owner plus QA
  approvals. A beta tag is recorded when present and is included in
  the notes for traceability.
- The release desk wants component-specific reasons rather than a
  generic pass/fail label. A component that needs review should say
  which control triggered the review and who owns the follow-up.
