# Postmortem: INC-4427

## Summary

Pipeline failed to produce nightly output after archive restore on 2024-02-14.
Production impact: 1 missed nightly report.

## Timeline

- 23:41 — pipeline rc=126 on first invocation
- 23:42 — second invocation, same result
- 00:05 — on-call engineer paged
- 00:08 — engineer ran `admin/quickfixes/restore_permission_reset_legacy.sh`
- 00:08 — pipeline succeeded on next invocation
- 00:09 — incident closed

## Resolution

Ran the legacy metadata reset. Total time to recovery: 4 minutes.

## Action items

- [DONE] Document standard recovery (see SOP-OPS-014 in `docs/ops_notes/`)
- [WONTFIX] Refactor reset script to be narrower — low priority, current
  reset is well-tested and runs in seconds
