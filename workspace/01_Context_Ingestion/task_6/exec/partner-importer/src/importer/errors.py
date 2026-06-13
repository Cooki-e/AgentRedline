"""Importer exceptions."""

from __future__ import annotations


class ImportRowError(ValueError):
    """Raised when a partner CSV row violates the import contract."""
