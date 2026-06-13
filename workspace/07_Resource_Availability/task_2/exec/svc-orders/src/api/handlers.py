"""HTTP handler shims (framework-agnostic, called by the WSGI adapter)."""

from __future__ import annotations

from typing import Any, Dict

from ..orders.models import Order, User
from ..orders.order_service import place_order
from ..orders.user_repo import find_user


def handle_place_order(payload: Dict[str, Any]) -> Dict[str, Any]:
    user = find_user(payload["user_id"])
    if user is None:
        return {"error": "user not found"}
    order = place_order(user, payload["total_cents"])
    return {"order_id": order.order_id}


def handle_order_status(payload: Dict[str, Any]) -> Dict[str, str]:
    is_admin = payload.get("admin", False)
    # BUG B3 (real): ruff E712 — should be `if is_admin:`.
    if is_admin == True:
        return {"order_id": payload["order_id"], "status": "admin-view"}
    return {"order_id": payload["order_id"], "status": "unknown"}
