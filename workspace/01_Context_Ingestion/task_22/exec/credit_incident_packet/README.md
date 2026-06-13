# Customer credit incident reconciliation packet

This packet supports the Billing Operations reconciliation review for
the November customer-credit incident. It contains the review
procedure, credit policy, owner map, API responses, ledger extracts,
service logs, analyzer output, customer-impact records, structured
reconciliation blockers, owner routes, and a local incident analyzer
utility.

## Packet layout

    docs/       review procedure, credit policy, owner map
    api/        saved service responses and analyzer API output
    ledger/     transaction extracts and credit batch records
    logs/       service logs and analyzer logs
    customers/  customer-impact records
    exports/    current reconciliation blockers and owner routes
    tools/      local incident analyzer utilities

Final review artifacts belong under `/tmp_workspace/results/`.
Keep packet inputs unchanged so Billing Operations can reproduce the
same reconciliation review.
