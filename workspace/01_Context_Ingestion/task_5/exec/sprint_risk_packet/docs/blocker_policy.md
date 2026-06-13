# Blocker policy

A ticket counts as an active release blocker when:

- `Sprint` is `june-platform`;
- `CurrentStatus` is `blocked` or `needs-review`;
- `BlockerType` is not empty;
- `ResolutionState` is not `resolved`, `closed`, or `waived`;
- the latest event history does not show a later resolution.

Tickets with `CurrentStatus=done` are not active blockers. A blocker
remains active until the current ticket export and event history both
reflect resolution.
