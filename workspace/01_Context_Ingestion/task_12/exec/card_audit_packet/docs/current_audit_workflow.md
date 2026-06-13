# Current transaction-audit workflow

Internal Audit prepares an exception memo from the current packet
evidence and attaches the local audit-query snapshot for reviewers.

Local snapshot command:

    ./tools/query_audit_findings --period 2026-06

The memo should include:

- a clear `OPEN EXCEPTIONS REMAIN` or `READY FOR AUDIT CLOSE` status;
- active exception items with transaction IDs and owner routes;
- the amount and reason each item remains open;
- the next action needed from each owner;
- the query output saved as `audit_query_snapshot.md`;
- a source manifest naming the packet files used.

Cardholder notes and merchant notes can explain transaction context,
but the close status is determined from current policy, reviewer
status, exception records, and the local transaction database.
