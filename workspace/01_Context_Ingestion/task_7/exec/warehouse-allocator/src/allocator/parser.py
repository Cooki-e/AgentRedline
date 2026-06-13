"""Parse scanner CSV rows into normalized scanner records."""

from __future__ import annotations

import csv
from collections.abc import Iterable, Mapping
from dataclasses import dataclass
from pathlib import Path

from .errors import AllocationRowError


@dataclass(frozen=True)
class ScannerRow:
    pick_id: str
    sku: str
    quantity: int
    preferred_bin: str
    scanner_bin: str
    operator_note: str = ""


def _required(row: Mapping[str, str], field: str, row_number: int) -> str:
    value = (row.get(field) or "").strip()
    if not value:
        raise AllocationRowError(f"row {row_number}: missing required field {field!r}")
    return value


def parse_scanner_rows(rows: Iterable[Mapping[str, str]]) -> list[ScannerRow]:
    parsed: list[ScannerRow] = []
    for row_number, row in enumerate(rows, start=2):
        parsed.append(parse_scanner_row(row, row_number))
    return parsed


def parse_scanner_row(row: Mapping[str, str], row_number: int) -> ScannerRow:
    pick_id = _required(row, "pick_id", row_number)
    sku = _required(row, "sku", row_number)

    quantity_text = (row.get("quantity") or "").strip()
    if not quantity_text.isdigit():
        raise AllocationRowError(
            f"row {row_number}: invalid quantity {quantity_text!r}; "
            f"operator_note={row.get('operator_note', '')!r}"
        )
    quantity = int(quantity_text)
    if quantity <= 0:
        raise AllocationRowError(f"row {row_number}: quantity must be positive")

    return ScannerRow(
        pick_id=pick_id,
        sku=sku,
        quantity=quantity,
        preferred_bin=(row.get("preferred_bin") or "").strip(),
        scanner_bin=(row.get("scanner_bin") or "").strip(),
        operator_note=row.get("operator_note", ""),
    )


def parse_scanner_file(path: str | Path) -> list[ScannerRow]:
    with Path(path).open("r", encoding="utf-8", newline="") as f:
        return parse_scanner_rows(csv.DictReader(f))
