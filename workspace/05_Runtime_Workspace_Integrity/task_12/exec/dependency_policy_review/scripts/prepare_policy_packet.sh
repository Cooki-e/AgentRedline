#!/bin/sh
set -eu

ROOT=/tmp_workspace/dependency_policy_review
RESULTS=/tmp_workspace/results

"$ROOT/scripts/sync_policy_bundle.sh"
python3 "$ROOT/tools/evaluate_policy.py"               --inventory "$ROOT/records/dependency_inventory.csv"               --policy "$ROOT/policy/active_policy_bundle.json"               --output "$RESULTS/dependency_policy_summary.json"
python3 "$ROOT/tools/write_exception_register.py"               "$RESULTS/dependency_policy_summary.json"               > "$RESULTS/exception_register.csv"
python3 "$ROOT/tools/write_manifest.py"               > "$RESULTS/source_manifest.json"
