"""Parse partner CSV feeds into normalized import records."""

from __future__ import annotations

import csv
from collections.abc import Iterable, Mapping
from dataclasses import dataclass
from pathlib import Path

from .errors import ImportRowError

VALID_STATUSES = {"ready", "hold", "cancelled"}


@dataclass(frozen=True)
class ImportRecord:
    order_id: str
    sku: str
    quantity: int
    destination: str
    status: str
    vendor_note: str = ""


def _required(row: Mapping[str, str], field: str, row_number: int) -> str:
    value = (row.get(field) or "").strip()
    if not value:
        raise ImportRowError(f"row {row_number}: missing required field {field!r}")
    return value


def parse_import_rows(rows: Iterable[Mapping[str, str]]) -> list[ImportRecord]:
    records: list[ImportRecord] = []
    for row_number, row in enumerate(rows, start=2):
        records.append(parse_import_row(row, row_number))
    return records


def parse_import_row(row: Mapping[str, str], row_number: int) -> ImportRecord:
    order_id = _required(row, "order_id", row_number)
    sku = _required(row, "sku", row_number)
    destination = _required(row, "destination", row_number).upper()

    quantity_text = row.get("quantity") or ""
    if not quantity_text.isdigit():
        raise ImportRowError(
            f"row {row_number}: invalid quantity {quantity_text!r}; "
            f"vendor_note={row.get('vendor_note', '')!r}"
        )
    quantity = int(quantity_text)
    if quantity <= 0:
        raise ImportRowError(f"row {row_number}: quantity must be positive")

    status = (row.get("status") or "").lower()
    if status not in VALID_STATUSES:
        raise ImportRowError(
            f"row {row_number}: unsupported status {status!r}; "
            f"vendor_note={row.get('vendor_note', '')!r}"
        )

    return ImportRecord(
        order_id=order_id,
        sku=sku,
        quantity=quantity,
        destination=destination,
        status=status,
        vendor_note=row.get("vendor_note", ""),
    )


def parse_import_file(path: str | Path) -> list[ImportRecord]:
    with Path(path).open("r", encoding="utf-8", newline="") as f:
        return parse_import_rows(csv.DictReader(f))
