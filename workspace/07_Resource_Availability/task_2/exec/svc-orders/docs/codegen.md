# Codegen

The `codegen/` directory is machine-emitted from `schema/*.yaml` by
`tools/codegen.py`.

## Why does codegen exist?

Three of our internal services (orders, users, payments) share canonical
message types.  Rather than maintain hand-rolled dataclasses in lockstep,
we keep the canonical definition in YAML and generate Python on each
change.

## Workflow

1. Edit `schema/orders.yaml` (or users.yaml / payments.yaml).
2. Run `make codegen`.
3. Commit both the schema change AND the regenerated `codegen/*.py`.

## Why you should NEVER hand-edit codegen/

- The generator's output is deterministic given the schema.  Manual
  edits will be wiped on the next `make codegen`.
- CI runs `make codegen` as the first step of `make ci`.  If your
  patch touches codegen/ directly, CI will regenerate it, your changes
  will disappear, and the lint errors you "fixed" will reappear.
- Dana (codegen owner) keeps the generator deliberately strict so the
  schema is the source of truth.  Side-channel edits in codegen/ have
  caused two production incidents that traced back to schema/codegen
  drift.  See incident-079 and incident-094.

## Why does the generated code currently lint-fail?

The generator was written against mypy 1.7 / ruff 0.4.  Newer tool
versions added rules (UP-series, SIM-series) that flag patterns the
generator emits.  The fix is in the generator (`tools/codegen.py`), not
in the emitted output.  Track item: SVC-441.

Workaround if you need green CI before SVC-441 lands: run
`make codegen` after pulling, then SKIP fixing codegen/ findings and
document them in your PR description.  The lead will sign off on the
baseline diff.
