"""Allocation service and summary helpers."""

from __future__ import annotations

import json
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

from .parser import ScannerRow, parse_scanner_file, parse_scanner_rows
from .rules import choose_allocation_bin


@dataclass(frozen=True)
class Allocation:
    pick_id: str
    sku: str
    quantity: int
    allocated_bin: str


def load_default_bins(path: str | Path) -> dict[str, str]:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def allocate_parsed_rows(
    rows: list[ScannerRow],
    default_bins: dict[str, str],
) -> list[Allocation]:
    allocations: list[Allocation] = []
    for row in rows:
        allocations.append(
            Allocation(
                pick_id=row.pick_id,
                sku=row.sku,
                quantity=row.quantity,
                allocated_bin=choose_allocation_bin(row, default_bins),
            )
        )
    return allocations


def allocate_rows(
    rows: list[dict[str, str]],
    default_bins: dict[str, str],
) -> list[Allocation]:
    return allocate_parsed_rows(parse_scanner_rows(rows), default_bins)


def allocate_file(
    scanner_path: str | Path,
    default_bins_path: str | Path,
) -> list[Allocation]:
    return allocate_parsed_rows(
        parse_scanner_file(scanner_path),
        load_default_bins(default_bins_path),
    )


def summarize_allocations(allocations: list[Allocation]) -> dict[str, object]:
    by_bin = Counter(allocation.allocated_bin for allocation in allocations)
    total_quantity = sum(allocation.quantity for allocation in allocations)
    return {
        "allocation_count": len(allocations),
        "total_quantity": total_quantity,
        "bins": dict(sorted(by_bin.items())),
    }


def summarize_batch(
    scanner_path: str | Path,
    default_bins_path: str | Path,
) -> dict[str, object]:
    return summarize_allocations(allocate_file(scanner_path, default_bins_path))
