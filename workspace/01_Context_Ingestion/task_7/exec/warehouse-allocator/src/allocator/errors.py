"""Allocator exceptions."""

from __future__ import annotations


class AllocationRowError(ValueError):
    """Raised when a scanner row violates the allocation contract."""
