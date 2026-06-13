"""Render accepted orders for the warehouse fulfillment handoff."""

from __future__ import annotations

from collections.abc import Iterable, Mapping
from typing import Any


def format_order_row(order: Mapping[str, Any]) -> str:
    """Render one accepted order without changing export row count."""
    order_id = str(order["order_id"]).strip()
    customer_name = str(order["customer_name"]).strip()
    warehouse_code = str(order["warehouse_code"]).strip().upper()
    delivery_note = order["delivery_note"].strip()
    return "|".join((order_id, customer_name, warehouse_code, delivery_note))


def render_fulfillment_export(orders: Iterable[Mapping[str, Any]]) -> str:
    """Render exactly one line per accepted order."""
    return "\n".join(format_order_row(order) for order in orders)
