#!/bin/sh
set -eu

ROOT=/tmp_workspace/source_attestation
RESULTS=/tmp_workspace/results

"$ROOT/scripts/configure_trusted_status.sh"
python3 "$ROOT/tools/evaluate_source_attestations.py"               --root "$ROOT"               --output "$RESULTS/source_attestation_summary.json"
python3 "$ROOT/tools/write_review_notes.py"               "$RESULTS/source_attestation_summary.json"               > "$RESULTS/review_notes.md"
python3 "$ROOT/tools/write_manifest.py"               > "$RESULTS/source_manifest.json"
