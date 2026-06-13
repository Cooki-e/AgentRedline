"""
Reconciliation utilities for migrated billing ledger rows.

The reconciliation report compares invoice totals against migrated
posting totals. The rounding mismatch in MIG-517 remains open for
multi-currency invoices.
"""

from __future__ import annotations


def compare_totals(invoice_total: int, posting_total: int) -> int:
    return posting_total - invoice_total
