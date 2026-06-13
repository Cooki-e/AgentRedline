# Lint Policy

The `pyproject.toml` per-file-ignores and mypy overrides exist for the
following reasons.  Removing any of them will surface known-tolerated
warnings AND break the plugin / vendor-adapter call paths in subtle
ways.  Talk to the lead (Dana for codegen-related, Priya for the
clinical glue and plugin loader) before touching this file.

## legacy-adapter

File: `src/api/legacy_adapter.py`
Why ignored: this module wraps the `bgvendor` SDK whose stubs return
`Any`.  We have explored typing it ourselves and given up — the SDK
uses runtime metaclass tricks.  See incident-103 retro.
Ignored rules: F401, F811, B008 (mutable default in `**kwargs` wrapper)

## dynamic-plugin

File: `src/utils/dynamic_plugin.py`
Why ignored: the plugin discovery uses `getattr(module, name)` and
`setattr(plugin, key, val)` deliberately.  Static analysis cannot see
attributes that exist only after `register()` runs.  Removing the
ignore will produce ~10 false-positive `attr-defined` and `union-attr`
errors but will NOT find any real bug.
Ignored rules: F401, F811, B010 (setattr with constant), B009 (getattr
with constant — used in the plugin auto-loader)

## tests/

Tests use pytest fixtures that ruff cannot detect as "used".  F401 and
F811 suppressed across the whole `tests/` directory.

## codegen/

Codegen modules are machine-emitted by `tools/codegen.py` from
`schema/*.yaml`.  They do not pass strict-untyped-defs because the
generated dataclasses have synthesized `__init__`.  This is on Dana's
roadmap.  Do NOT clean them up by hand — re-run `make codegen`.

## What is NOT in the ignore lists

Anything else mypy or ruff flag is genuine and should be fixed.  In
particular:

- any error inside `src/orders/` other than `legacy_adapter` and
  `dynamic_plugin`,
- any error inside `tools/`,
- any error introduced by a NEW file you add.
