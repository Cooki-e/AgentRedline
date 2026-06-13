"""Order-domain model."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Order:
    order_id: str
    customer_name: str
    warehouse_code: str
    delivery_note: str | None = None
