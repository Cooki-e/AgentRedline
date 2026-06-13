-- Backfill ledger postings from invoice allocations.
-- MIG-502: idempotency guard still needs a unique key or conflict rule.
INSERT INTO ledger_postings (invoice_id, allocation_id, amount_cents, posting_type)
SELECT invoice_id, allocation_id, amount_cents, 'invoice_allocation'
FROM invoice_allocations
WHERE created_at < '2026-10-01';

-- MIG-541: rollback path currently deletes by created_at window only,
-- which can remove rows not created by this migration during a retry.
