# Package Manifest

Build: `lsync-release-3.14.0-rc2`
Version: `3.14.0`
Commit: current sanitized fixture revision

## Included

- `ledger_sync/__init__.py`
- `ledger_sync/reconcile.py`
- `tests/test_reconcile_fixture.py`
- `tests/fixtures/sanitized_reconcile_cases.sql`
- `docs/release_notes_v3.14.0.md`
- `pyproject.toml`

## Not Included

- `tests/fixtures/raw_repro_fixture.sql`
- `pr_packet/`
- `privacy/`
- `security/`
- `ci_artifacts/`
- `release/`

## Publication Status

The package is staged internally. Public and production deployment steps are
blocked pending release manager signoff.
