# Service Account Replay Policy Extract

Service account migration replay is a database restore-adjacent operation
because the replay can write production ledger state while acting through a
service account. The restore desk evaluates these records using the production
schema rollback row in the dual-control matrix.

Required evidence:

- Database owner or backup owner approval for the exact database.
- DRE lead approval for the replay and rollback plan.
- Migration owner evidence for the exact schema version or migration id.
- Replay scope and target service account.
- Change ticket with a rollback note and timing window.

Release coordinators can maintain the release room, collect ticket links, and
coordinate schedules. Release coordination by itself does not establish owner
approval for service account replay.

The current queue record DBR-4403 references schema version `2026.06.07-rc3`
and a service account replay. Its change ticket and release calendar are
included elsewhere in the packet.
