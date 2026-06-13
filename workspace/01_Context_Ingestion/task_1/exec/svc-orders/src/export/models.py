"""Export-facing types."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ExportBatch:
    warehouse_code: str
    rendered_rows: str

    @property
    def row_count(self) -> int:
        return 0 if not self.rendered_rows else len(self.rendered_rows.splitlines())
