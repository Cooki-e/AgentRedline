"""Input validation for required order-export fields."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

REQUIRED_FIELDS = ("order_id", "customer_name", "warehouse_code")


def missing_required_fields(order: Mapping[str, Any]) -> list[str]:
    return [field for field in REQUIRED_FIELDS if not order.get(field)]
