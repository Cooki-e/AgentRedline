#!/bin/sh
set -eu

ROOT=/tmp_workspace/trial_query_resolution
RESULTS=/tmp_workspace/results

python3 "$ROOT/scripts/normalize_source_extracts.py"
python3 "$ROOT/tools/evaluate_queries.py"               --root "$ROOT"               --output "$RESULTS/query_listing.csv"
python3 "$ROOT/tools/write_summary.py"               "$ROOT/source_data/subjects.csv"               "$RESULTS/query_listing.csv"               "$ROOT/source_data/site_notes.md"               > "$RESULTS/query_summary.md"
python3 "$ROOT/tools/write_manifest.py"               > "$RESULTS/source_manifest.json"
