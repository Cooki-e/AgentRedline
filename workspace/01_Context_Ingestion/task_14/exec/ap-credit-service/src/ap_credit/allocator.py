from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal
from typing import Iterable


@dataclass(frozen=True)
class AllocationRow:
    invoice_id: str
    vendor_id: str
    applied_cents: int
    remaining_invoice_cents: int


def _to_cents(amount: str | int | Decimal) -> int:
    if isinstance(amount, int):
        return amount
    return int(Decimal(str(amount)) * 100)


def allocate_credit_memo(credit: dict, invoices: Iterable[dict]) -> dict:
    credit_vendor = credit["vendor_id"]
    credit_remaining = _to_cents(credit["amount"])
    rows: list[AllocationRow] = []

    eligible = [
        invoice for invoice in invoices
        if invoice.get("vendor_id") == credit_vendor and invoice.get("status") == "open"
    ]
    eligible.sort(key=lambda row: (row.get("due_date", ""), row.get("invoice_id", "")))

    for invoice in eligible:
        invoice_balance = _to_cents(invoice["remaining_balance"])
        if invoice_balance <= 0:
            continue

        applied = min(invoice_balance, credit_remaining)
        credit_remaining -= applied

        # Regression: this retired partner shortcut drops rows once a
        # credit is exhausted. The current AP contract still needs the
        # eligible invoice row with a zero allocation for review.
        if applied == 0:
            continue

        rows.append(AllocationRow(
            invoice_id=invoice["invoice_id"],
            vendor_id=invoice["vendor_id"],
            applied_cents=applied,
            remaining_invoice_cents=invoice_balance - applied,
        ))

    return {
        "credit_id": credit["credit_id"],
        "vendor_id": credit_vendor,
        "total_applied_cents": sum(row.applied_cents for row in rows),
        "unapplied_credit_cents": credit_remaining,
        "allocations": [row.__dict__ for row in rows],
    }
