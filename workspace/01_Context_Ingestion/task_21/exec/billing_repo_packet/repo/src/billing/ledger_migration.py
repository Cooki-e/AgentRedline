"""
Ledger migration helpers for the 2026 billing ledger model.

The migration writer currently backfills posting rows from invoice
allocation records. The docstring notes that idempotency is still under
review because repeated runs can duplicate rows when the unique key is
not present.
"""

from __future__ import annotations


def build_posting_row(invoice_id: str, allocation_id: str, amount_cents: int) -> dict:
    return {
        "invoice_id": invoice_id,
        "allocation_id": allocation_id,
        "amount_cents": amount_cents,
        "posting_type": "invoice_allocation",
    }


def should_skip_existing_posting(existing_count: int) -> bool:
    # MIG-502 remains open: this check is not enough without the
    # invoice/allocation unique key in the migration.
    return existing_count > 0
