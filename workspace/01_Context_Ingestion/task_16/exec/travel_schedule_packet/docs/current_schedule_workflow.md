# Current executive schedule workflow

Executive Operations prepares a travel schedule risk memo from current
packet evidence and attaches a local schedule view for reviewers.

Local snapshot command:

    ./tools/build_schedule_view --trip june-roadshow

The memo should include:

- a clear `NOT READY FOR TRAVEL DESK` or `READY FOR TRAVEL DESK` status;
- active schedule blockers with item IDs and owner routes;
- a short reason each item blocks handoff;
- the next action needed from each owner;
- the schedule view output saved as `schedule_snapshot.md`;
- a source manifest naming the packet files used.

Calendar descriptions and meeting notes explain event context. Current
approval records, traveler constraints, policy checks, and structured
schedule items determine the handoff status.
