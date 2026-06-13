# Contributing

Migration changes require:

- an idempotency check for repeated migration runs;
- a rollback test that restores ledger posting state;
- reconciliation evidence for invoice totals;
- owner routing for data backfill and observability gaps;
- CI evidence before release branch approval.
