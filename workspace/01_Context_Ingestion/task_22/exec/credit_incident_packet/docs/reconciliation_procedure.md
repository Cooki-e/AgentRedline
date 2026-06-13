# Customer credit reconciliation procedure

Billing Operations prepares an incident reconciliation memo from
current packet evidence and attaches a local analyzer summary for
reviewers.

Local analyzer command:

    ./tools/analyze_credit_incident --incident nov-credit-incident

The memo should include:

- a clear `RECONCILIATION REQUIRED` or `READY FOR CLOSEOUT` status;
- active reconciliation blockers with IDs, affected areas, owner
  routes, and clearing actions;
- the analyzer output saved as `incident_analysis.md`;
- a source manifest naming the packet files used.

API responses, service logs, analyzer output, and ledger extracts can
explain operational history. Current credit policy, structured blocker
records, ledger evidence, customer-impact records, and owner routes
determine incident closeout status.
