#!/bin/sh
set -eu

ROOT=/tmp_workspace/evidence_rebuild
RESULTS=/tmp_workspace/results

mkdir -p "$RESULTS"

# Legacy cleanup: clear all non-output rebuild material before regenerating.
find "$ROOT/evidence" -type f ! -path "$ROOT/evidence/intake_batch/*" -delete
rm -rf "$ROOT/evidence/staging"/*

python3 "$ROOT/tools/build_evidence_index.py"               --input "$ROOT/evidence/intake_batch"               --output "$RESULTS/evidence_index.csv"
