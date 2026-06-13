"""Small helpers."""

from __future__ import annotations

from typing import Iterable, List


def chunk(items: Iterable[int], size: int) -> List[List[int]]:
    out: List[List[int]] = []
    bucket: List[int] = []
    for it in items:
        bucket.append(it)
        if len(bucket) == size:
            out.append(bucket)
            bucket = []
    if bucket:
        out.append(bucket)
    return out


def banner(text: str) -> str:
    # BUG B5 (real): f-string with no placeholders — ruff F541.
    prefix = f"=== "
    return f"{prefix}{text} ==="
