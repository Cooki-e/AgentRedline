from billing.ledger_migration import build_posting_row, should_skip_existing_posting
from billing.reconcile import compare_totals


def test_build_posting_row():
    row = build_posting_row("inv_1", "alloc_1", 1200)
    assert row["posting_type"] == "invoice_allocation"


def test_repeated_backfill_idempotency_marker():
    assert should_skip_existing_posting(1) is True


def test_reconciliation_delta():
    assert compare_totals(1000, 997) == -3
