"""In-memory repository used by examples."""

from __future__ import annotations

from .models import Order


class OrderRepository:
    def __init__(self) -> None:
        self._orders: list[Order] = []

    def add(self, order: Order) -> None:
        self._orders.append(order)

    def all(self) -> list[Order]:
        return list(self._orders)
