# Release gate policy

A release is ready for handoff only when all of the following are true:

1. no ticket in the release export has an active `blocker` label;
2. required CI jobs are passing for the release manifest revision;
3. required approvals are present and current;
4. release-note and customer-facing text reviews are complete.

A blocker remains active until current packet evidence records a
resolved ticket state, a passing CI replacement, or a completed
approval. Discussion notes alone do not close blockers.

If any active blocker remains, the handoff disposition is
`NOT READY FOR HANDOFF`.
