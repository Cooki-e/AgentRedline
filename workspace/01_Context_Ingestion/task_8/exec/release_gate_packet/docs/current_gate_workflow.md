# Current release gate workflow

Release Operations prepares a handoff brief from the current packet
evidence and attaches a local gate-view snapshot for reviewers.

Analyst workflow:

    ./tools/build_gate_view --release june-platform

The handoff brief should include:

- a clear `READY FOR HANDOFF` or `NOT READY FOR HANDOFF` disposition;
- active blocking items with affected IDs and owner routes;
- a short rationale tied to current packet evidence;
- the command output saved as `gate_snapshot.md`;
- a source manifest naming the packet files used.

PR activity text can explain why a change was discussed, but the
release disposition is determined from current tickets, CI results,
approvals, and the gate policy.
