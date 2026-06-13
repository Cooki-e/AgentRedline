"""Import-service aggregation helpers."""

from __future__ import annotations

from collections import Counter
from pathlib import Path

from .parser import ImportRecord, parse_import_file


def summarize_records(records: list[ImportRecord]) -> dict[str, object]:
    by_destination = Counter(record.destination for record in records)
    total_quantity = sum(record.quantity for record in records)
    ready_count = sum(1 for record in records if record.status == "ready")
    return {
        "record_count": len(records),
        "total_quantity": total_quantity,
        "ready_count": ready_count,
        "destinations": dict(sorted(by_destination.items())),
    }


def summarize_import_file(path: str | Path) -> dict[str, object]:
    return summarize_records(parse_import_file(path))
