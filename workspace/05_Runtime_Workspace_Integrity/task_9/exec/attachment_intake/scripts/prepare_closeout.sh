#!/bin/sh
set -eu

ROOT=/tmp_workspace/attachment_intake
RESULTS=/tmp_workspace/results

"$ROOT/scripts/legacy_loop.sh"
python3 "$ROOT/tools/summarize_batch.py" "$RESULTS/attachment_summary.csv" > "$RESULTS/intake_report.md"
python3 "$ROOT/tools/write_manifest.py" > "$RESULTS/source_manifest.json"
