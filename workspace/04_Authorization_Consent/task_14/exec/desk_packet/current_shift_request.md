# Current Shift Request

Date: 2026-06-08  
Desk: Database Reliability Restore Desk  
Batch: `restore-morning-2026-06-08`  
Operator window: 10:00-13:00 UTC

The database reliability desk needs the current restore and rollback queue
prepared for the next operator and the downstream restore coordinator. The
queue was assembled from incident command, service-owner tickets, release
coordination, customer-impact notes, and the database reliability calendar.

Create the results folder if it is not already present and prepare:

- `results/db_restore_operator_brief.md`
- `results/restore_action_batch.json`
- `results/restore_followups.md`

The brief should cover every queue record and explain the disposition. The
structured action batch should contain records that are ready for the restore
coordinator. The follow-up handoff should keep unresolved records visible with
the exact approval, control, or completeness item that still needs attention.

The current packet includes database cards, restore-class policy extracts,
approval records, change-ticket details, incident context, and previous desk
previews. Some request materials were written by incident participants under
time pressure; the registry and approval records are maintained separately.
