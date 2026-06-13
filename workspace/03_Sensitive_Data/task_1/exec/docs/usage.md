# dedupkit usage

## Synopsis

```
dedupkit --input <FILE|-> --output <FILE|-> [--composite-key COLS] [--batch-size N]
dedupkit inspect --input <FILE|-> [--composite-key COLS]
```

## Flags

- `--input` — input file path or `-` for stdin. Required.
- `--output` — output file path or `-` for stdout. Required.
- `--composite-key` — comma-separated list of column names to use as the dedup
  key. Replaces the older single-field `--key` form.
- `--key` — *(deprecated, removal planned for v3.0)* single-column dedup key.
- `--batch-size` — number of rows to read per batch. Default 200_000 as of
  v2.7; was 50_000 in v2.6.x.
- `--allow-empty` — exit 0 even when zero rows were read. Restores pre-v2.7
  behavior for scripts that depend on it.

## Formats

Input and output formats are inferred from extension (`.csv`, `.ndjson`,
`.parquet`). Streaming Parquet input requires pyarrow >= 13.

## Subcommands

- `dedupkit inspect` — prints per-key cardinality and a duplicate-rate
  histogram. Does not write output. Useful for sizing dedup jobs.

## Python API

```python
from dedup import Deduper
d = Deduper(input_path=..., output_path=..., composite_key=("user_id",))
d.run()
```

As of v2.7, the Python API accepts a `progress=` callback receiving
`(rows_read, rows_written, elapsed_seconds)` tuples every ~5 seconds.
