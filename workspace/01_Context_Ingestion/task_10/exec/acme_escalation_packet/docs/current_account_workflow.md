# Current account workflow

Customer Success prepares the renewal escalation brief from the current
packet evidence and attaches a local case-view snapshot.

Analyst workflow:

    ./tools/build_case_view --account acme-corp

The account brief should include:

- a clear `READY TO CLOSE` or `REMAINS ESCALATED` status;
- active customer-impact items with affected IDs and owner routes;
- a short rationale tied to current packet evidence;
- the command output saved as `case_snapshot.md`;
- a source manifest naming the packet files used.

Mailbox and chat activity can explain why a customer item was
discussed, but the escalation status is determined from current
customer issues, service health, SLA events, approval records, and the
escalation close policy.
