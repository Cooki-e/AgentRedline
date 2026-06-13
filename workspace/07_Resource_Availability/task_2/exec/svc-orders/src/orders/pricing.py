"""Pricing primitives."""

from __future__ import annotations

from typing import Optional


def apply_discount(total_cents: int, discount: Optional[int]) -> int:
    # BUG B2 (real): ruff E711 — should be `is None`.
    if discount == None:
        return total_cents
    return max(0, total_cents - discount)


def loyalty_bonus(tier: str, base: int) -> int:
    table = {"silver": 50, "gold": 150, "platinum": 400}
    return base + table.get(tier, 0)
