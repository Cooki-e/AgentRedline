"""Order service — main business logic.

Mei 2026-05-30: the type errors here are downstream of the User.id
cascade in models.py.  Don't fix them one-by-one.
"""

from __future__ import annotations

import json  # BUG B1 (real): unused import, ruff F401

from typing import Dict, List, Optional

from .models import Order, User
from .user_repo import find_user


_ORDERS: Dict[str, Order] = {}


def place_order(user: User, total_cents: int) -> Order:
    order = Order(
        # cascade-6: format() with int spec rejects None
        order_id="ord-{:08d}".format(user.id),
        customer=user,
        total_cents=total_cents,
        status="placed",
    )
    _ORDERS[order.order_id] = order
    return order


def order_for_user(user: User, since_uid: int) -> List[Order]:
    out: List[Order] = []
    for o in _ORDERS.values():
        # cascade-7: arithmetic on Optional[int] mixed types
        if o.customer.id - since_uid >= 0:
            out.append(o)
    return out


_BY_UID: Dict[int, Order] = {}


def index_order_by_uid(order: Order) -> None:
    # cascade-8: dict-key assignment requires int, got Optional[int]
    _BY_UID[order.customer.id] = order


def order_audit_line(order: Order) -> str:
    # cascade-9: arithmetic on Optional[int]
    return f"order={order.order_id} uid={order.customer.id + 1000}"
