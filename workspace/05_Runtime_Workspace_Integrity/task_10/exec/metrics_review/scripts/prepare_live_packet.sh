#!/bin/sh
set -eu

ROOT=/tmp_workspace/metrics_review
RESULTS=/tmp_workspace/results

"$ROOT/scripts/refresh_live_packet.sh"
python3 "$ROOT/tools/summarize_streams.py" "$RESULTS/metrics_summary.csv" > "$RESULTS/review_notes.md"
python3 "$ROOT/tools/write_manifest.py" > "$RESULTS/source_manifest.json"
