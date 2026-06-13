from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class SettlementEvent:
    invoice_id: str
    customer_ref: str
    amount: Decimal
    event_type: str
    provider_attempt: int
    credit_memo_ref: str | None = None


@dataclass(frozen=True)
class LedgerEntry:
    invoice_id: str
    customer_ref: str
    open_amount: Decimal
    status: str
    credit_memo_ref: str | None = None


def reconcile_event(event: SettlementEvent, entries: list[LedgerEntry]) -> str:
    candidates = [
        entry for entry in entries
        if entry.invoice_id == event.invoice_id
        and entry.customer_ref == event.customer_ref
        and entry.status in {"open", "pending_credit"}
    ]
    if event.credit_memo_ref:
        candidates = [
            entry for entry in candidates
            if entry.credit_memo_ref == event.credit_memo_ref
        ]
    if not candidates:
        return "unmatched"
    if event.provider_attempt > 1 and event.event_type == "settlement_retry":
        return "retry_ignored"
    if sum(entry.open_amount for entry in candidates) == event.amount:
        return "matched"
    return "needs_review"
