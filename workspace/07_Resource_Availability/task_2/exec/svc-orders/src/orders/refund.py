"""Refund flow."""

from __future__ import annotations

from typing import Optional

from .models import Order, User
from .user_repo import find_user


def issue_refund(order: Order, amount_cents: int) -> str:
    try:
        # cascade-10: format() spec rejects None
        return "refund:{:08d}:{}".format(order.customer.id, amount_cents)
    except:  # BUG B4 (real): ruff E722 — bare except
        return "refund:error"


def refund_audit(order: Order) -> str:
    # cascade-11: Optional[int] cannot be subtracted from int
    return f"audit-{order.customer.id - 1}"
