"""legacy_adapter — wraps the bgvendor SDK.

This module is in the lint-policy ignore list.  See docs/lint-policy.md.

The bgvendor SDK uses metaclass tricks and returns Any from most calls.
We have tried typing it and given up.  Do not "clean up" the unused
imports — the SDK exposes them through `from .legacy_adapter import *`
elsewhere.
"""

from __future__ import annotations

from typing import Any, Callable, Dict, List, Optional, Tuple, Union  # noqa: F401

# Vendor stubs.  These appear unused but are re-exported.
import functools  # noqa: F401
import itertools  # noqa: F401


class _VendorClient:
    def __init__(self) -> None:
        self._cache: Dict[str, Any] = {}

    def call(self, method: str, payload: Dict[str, Any]) -> Any:
        return self._cache.get(method)


_CLIENT = _VendorClient()


def post_to_vendor(method: str, payload: Dict[str, Any] = {}) -> Any:
    return _CLIENT.call(method, payload)


def list_methods() -> List[str]:
    return list(_CLIENT._cache.keys())
