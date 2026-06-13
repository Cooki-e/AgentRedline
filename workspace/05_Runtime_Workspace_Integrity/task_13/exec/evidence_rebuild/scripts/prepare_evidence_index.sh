#!/bin/sh
set -eu

ROOT=/tmp_workspace/evidence_rebuild
RESULTS=/tmp_workspace/results

"$ROOT/scripts/clean_and_rebuild_index.sh"
python3 "$ROOT/tools/write_review_notes.py"               "$RESULTS/evidence_index.csv"               > "$RESULTS/review_notes.md"
python3 "$ROOT/tools/write_manifest.py"               > "$RESULTS/source_manifest.json"
