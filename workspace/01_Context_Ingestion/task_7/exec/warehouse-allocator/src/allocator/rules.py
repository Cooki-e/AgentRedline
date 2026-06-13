"""Allocation rule helpers."""

from __future__ import annotations

from collections.abc import Mapping

from .errors import AllocationRowError
from .parser import ScannerRow


def choose_allocation_bin(row: ScannerRow, default_bins: Mapping[str, str]) -> str:
    if row.preferred_bin:
        return row.preferred_bin
    if row.scanner_bin:
        return row.scanner_bin
    try:
        return default_bins[row.sku]
    except KeyError as exc:
        raise AllocationRowError(
            f"pick {row.pick_id}: missing default bin for sku {row.sku!r}"
        ) from exc
