"""Order-event dispatch service."""

from __future__ import annotations

from typing import Any


class OrderEventService:
    """Minimal in-memory service used by the receiver and local tests."""

    def __init__(self) -> None:
        self.events: list[dict[str, Any]] = []

    def process(self, payload: dict[str, Any]) -> None:
        self.events.append(payload)
