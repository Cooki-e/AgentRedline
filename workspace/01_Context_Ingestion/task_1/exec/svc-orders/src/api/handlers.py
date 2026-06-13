"""Tiny API facade used by local tests and examples."""

from __future__ import annotations

from collections.abc import Iterable, Mapping
from typing import Any

from src.export.service import create_warehouse_batch


def export_orders(
    orders: Iterable[Mapping[str, Any]],
    warehouse_code: str,
) -> dict[str, Any]:
    batch = create_warehouse_batch(orders, warehouse_code)
    return {
        "warehouse_code": batch.warehouse_code,
        "row_count": batch.row_count,
        "payload": batch.rendered_rows,
    }
