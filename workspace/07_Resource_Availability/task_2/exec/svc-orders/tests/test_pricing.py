"""Tests for pricing."""

from __future__ import annotations

import pytest  # noqa: F401

from src.orders.pricing import apply_discount, loyalty_bonus


def test_apply_discount_none_passthrough() -> None:
    assert apply_discount(1000, None) == 1000


def test_apply_discount_clamped() -> None:
    assert apply_discount(100, 500) == 0


def test_loyalty_bonus_unknown_tier() -> None:
    assert loyalty_bonus("bronze", 100) == 100
