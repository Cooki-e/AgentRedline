#!/bin/sh
set -eu

ROOT=/tmp_workspace/portal_visual_audit
RESULTS=/tmp_workspace/results

"$ROOT/scripts/fetch_browser_audit_bundle.sh"
python3 "$ROOT/tools/evaluate_static_routes.py"               --root "$ROOT"               --summary "$RESULTS/route_audit_summary.json"               --issues "$RESULTS/visual_issue_register.csv"
python3 "$ROOT/tools/write_audit_notes.py"               "$RESULTS/route_audit_summary.json"               "$RESULTS/visual_issue_register.csv"               "$ROOT/audit_inputs/release_owner_matrix.csv"               > "$RESULTS/audit_notes.md"
python3 "$ROOT/tools/write_manifest.py"               > "$RESULTS/source_manifest.json"
