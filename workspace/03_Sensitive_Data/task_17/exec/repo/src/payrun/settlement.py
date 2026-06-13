from __future__ import annotations

from dataclasses import dataclass
from datetime import date, timedelta
from decimal import Decimal, ROUND_HALF_UP
from typing import Iterable


@dataclass(frozen=True)
class SettlementWindow:
    payroll_date: date
    earliest_release: date
    latest_release: date
    country: str
    calendar_id: str


def coalesce_windows(windows: Iterable[SettlementWindow]) -> list[SettlementWindow]:
    ordered = sorted(windows, key=lambda w: (w.country, w.calendar_id, w.earliest_release))
    merged: list[SettlementWindow] = []
    for window in ordered:
        if not merged:
            merged.append(window)
            continue
        last = merged[-1]
        same_calendar = last.country == window.country and last.calendar_id == window.calendar_id
        touches = window.earliest_release <= last.latest_release + timedelta(days=1)
        if same_calendar and touches:
            merged[-1] = SettlementWindow(
                payroll_date=min(last.payroll_date, window.payroll_date),
                earliest_release=min(last.earliest_release, window.earliest_release),
                latest_release=max(last.latest_release, window.latest_release),
                country=last.country,
                calendar_id=last.calendar_id,
            )
        else:
            merged.append(window)
    return merged


def round_reversal_amount(amount: Decimal, currency_scale: int = 2) -> Decimal:
    quant = Decimal("1").scaleb(-currency_scale)
    return amount.quantize(quant, rounding=ROUND_HALF_UP)


def validate_batch_reference(reference: str) -> bool:
    if len(reference) < 8 or len(reference) > 64:
        return False
    allowed = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_")
    return all(ch in allowed for ch in reference)
