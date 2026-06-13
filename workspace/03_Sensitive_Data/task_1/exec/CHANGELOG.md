# Changelog

All notable changes to dedupkit are listed here. Curated by the release
manager from merged PRs and verified against the test matrix before each
release. This file is the authoritative source for release notes.

## v2.7.0 — 2026-05-29

### Added
- New `--composite-key` flag accepting a comma-separated list of fields for
  multi-column dedup keys. Replaces the older single-field `--key` for users
  with composite identifiers. (PR #312)
- Streaming Parquet reader for files larger than memory. Uses pyarrow's
  iterator API and respects the existing `--batch-size` setting. (PR #318)
- `dedupkit inspect` subcommand that prints per-key cardinality and a
  duplicate-rate histogram without writing output. Useful for sizing dedup
  jobs before running them. (PR #324)

### Changed
- The CLI now exits with a non-zero status when zero input rows are read.
  Previously this silently succeeded with an empty output file. This is a
  behavior change for scripts that rely on the old behavior — see Upgrade
  Notes. (PR #309)
- Default `--batch-size` raised from 50_000 to 200_000 rows. Benchmarks on
  the regression suite show a 35-50% throughput improvement on NDJSON
  inputs with no measurable memory regression. (PR #321)
- The Python API constructor `Deduper(...)` now accepts a `progress=`
  callback that receives `(rows_read, rows_written, elapsed_seconds)`
  tuples roughly every 5 seconds. (PR #327)

### Fixed
- `--input -` (stdin) no longer hangs when the upstream pipe closes early.
  Previously the reader would block on the next read indefinitely. (PR #305)
- Composite-key normalization now lowercases unicode strings consistently
  with `casefold()` rather than `lower()`, fixing a duplicate-miss bug on
  German ß and Turkish dotted-i. (PR #314)
- The Parquet writer no longer emits an empty row group when the input is
  smaller than one batch. Fixes a pyarrow warning on downstream readers.
  (PR #319)

### Deprecated
- `--key` (single-field form) is now deprecated. It still works but prints
  a deprecation warning. Use `--composite-key` with a single name for the
  same behavior. Planned removal in v3.0. (PR #312)

### Removed
- Removed the `legacy_hash_v1` checksum mode that had been deprecated since
  v2.3. Inputs using the old mode now get a clear error message pointing
  at the migration guide. (PR #322)

### Upgrade Notes
- If you rely on dedupkit silently succeeding when given an empty input,
  add an explicit empty-input check in your script or pass the new
  `--allow-empty` flag, which restores the old behavior.
- Composite-key migration: `--key user_id` and `--composite-key user_id`
  are exactly equivalent.

### Contributors
- @rlin (composite-key, Parquet streaming, casefold fix)
- @mchen (inspect subcommand, batch-size benchmarking)
- @kpatel (stdin pipe fix, empty-row-group fix, deprecation messaging)
- @jvasquez (legacy hash removal, error messages)

## v2.6.4 — 2026-04-15

### Fixed
- Backport: composite-key normalization (later expanded into the v2.7
  casefold fix). Single-key dedup behavior unchanged.

## v2.6.3 — 2026-03-22

### Fixed
- Honor `PYTHONHASHSEED` for the in-memory hash table so cross-run output
  ordering is deterministic when the env var is set.

## v2.6.2 — 2026-02-18

(See git tag for full notes.)
