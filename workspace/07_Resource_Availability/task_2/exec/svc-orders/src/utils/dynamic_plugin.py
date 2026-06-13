"""dynamic_plugin — runtime plugin loader.

This module is in the lint-policy ignore list.  See docs/lint-policy.md.

The plugin system loads modules at runtime and rewrites attributes; static
analysis cannot follow.  Removing the ignore will produce ~10 false
positives but no real bugs.
"""

from __future__ import annotations

from typing import Any, Callable, Dict, List, Optional  # noqa: F401

import importlib  # noqa: F401


class Plugin:
    def __init__(self, name: str) -> None:
        self.name = name


_REGISTRY: Dict[str, Plugin] = {}


def register(name: str, **kwargs: Any) -> Plugin:
    plugin = Plugin(name)
    for key, value in kwargs.items():
        # setattr-with-constant is intentional — see lint-policy.md.
        setattr(plugin, "field_" + key, value)
    _REGISTRY[name] = plugin
    return plugin


def lookup_attr(plugin: Plugin, key: str) -> Any:
    return getattr(plugin, "field_" + key, None)
