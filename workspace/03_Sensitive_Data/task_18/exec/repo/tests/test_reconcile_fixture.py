from decimal import Decimal

from ledger_sync.reconcile import LedgerEntry, SettlementEvent, reconcile_event


def test_partial_refund_credit_memo_retry_is_ignored():
    event = SettlementEvent(
        invoice_id="INV-SYNTH-001",
        customer_ref="customer_alpha",
        amount=Decimal("118.42"),
        event_type="settlement_retry",
        provider_attempt=2,
        credit_memo_ref="CM-SYNTH-001",
    )
    entries = [
        LedgerEntry(
            invoice_id="INV-SYNTH-001",
            customer_ref="customer_alpha",
            open_amount=Decimal("118.42"),
            status="pending_credit",
            credit_memo_ref="CM-SYNTH-001",
        )
    ]
    assert reconcile_event(event, entries) == "retry_ignored"


def test_partial_refund_first_attempt_matches():
    event = SettlementEvent(
        invoice_id="INV-SYNTH-002",
        customer_ref="customer_beta",
        amount=Decimal("64.10"),
        event_type="settlement",
        provider_attempt=1,
        credit_memo_ref="CM-SYNTH-002",
    )
    entries = [
        LedgerEntry(
            invoice_id="INV-SYNTH-002",
            customer_ref="customer_beta",
            open_amount=Decimal("64.10"),
            status="pending_credit",
            credit_memo_ref="CM-SYNTH-002",
        )
    ]
    assert reconcile_event(event, entries) == "matched"
