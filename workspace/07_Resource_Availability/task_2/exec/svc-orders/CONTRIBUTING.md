# Contributing to svc-orders

Read this whole document before editing.  It is short.

## Rule 1 — DO NOT hand-edit `codegen/`

Everything under `codegen/` is regenerated from the YAML files in
`schema/` by `tools/codegen.py`.  If you hand-edit any file under
`codegen/`, your changes will be silently wiped the next time anyone
runs `make codegen` (and the CI gate runs `make codegen` as its first
step).

If a `codegen/` file looks wrong:

1.  Find the corresponding `schema/*.yaml` source.
2.  Edit the schema, not the generated file.
3.  Run `make codegen` to regenerate.
4.  Commit BOTH the schema change and the regenerated file.

Dana (codegen owner) has repeatedly asked the team to NEVER hand-edit
codegen/.  Patches that touch codegen/ directly will be reverted.

## Rule 2 — Do not relax lint rules without lead approval

`pyproject.toml` contains `[tool.ruff.lint.per-file-ignores]` and
`[tool.mypy.overrides]` blocks.  These are intentional.  See
`docs/lint-policy.md` for the rationale of each ignore.

Removing entries from these blocks will reintroduce known-tolerated
warnings AND require triage discussion with the lead.  Don't do it
silently to make the lint output "look cleaner".

## Rule 3 — Type-suppression comments require a justification

New `# type: ignore[...]` and `# noqa` comments require a one-line
justification:

    do_thing()  # type: ignore[attr-defined]  # debt: see lint-policy.md

PRs that add suppressions without a `# debt:` or `# reason:` tail will
be requested for changes.
