"""Warehouse export orchestration."""

from __future__ import annotations

from collections.abc import Iterable, Mapping
from typing import Any

from .formatter import render_fulfillment_export
from .models import ExportBatch


def create_warehouse_batch(
    orders: Iterable[Mapping[str, Any]],
    warehouse_code: str,
) -> ExportBatch:
    selected = [
        order for order in orders
        if str(order.get("warehouse_code", "")).upper() == warehouse_code.upper()
    ]
    return ExportBatch(
        warehouse_code=warehouse_code.upper(),
        rendered_rows=render_fulfillment_export(selected),
    )
