# Billing service

The billing service stores customer invoices, payment allocations, and
ledger posting records. The `ledger-migration-2026` branch introduces
a new ledger posting model and a migration that backfills historical
posting records.

Reviewers should inspect migration SQL, posting code, idempotency
handling, rollback behavior, reconciliation tests, and CI output before
preparing the migration risk memo.
