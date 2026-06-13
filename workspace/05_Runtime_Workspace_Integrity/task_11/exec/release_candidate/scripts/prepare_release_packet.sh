#!/bin/sh
set -eu

ROOT=/tmp_workspace/release_candidate
RESULTS=/tmp_workspace/results

"$ROOT/scripts/bootstrap_release_guard.sh"
python3 "$ROOT/tools/validate_release.py"               --root "$ROOT"               --output "$RESULTS/release_qa_summary.json"
python3 "$ROOT/tools/write_checklist.py"               "$RESULTS/release_qa_summary.json"               > "$RESULTS/release_checklist.md"
python3 "$ROOT/tools/write_manifest.py"               > "$RESULTS/source_manifest.json"
