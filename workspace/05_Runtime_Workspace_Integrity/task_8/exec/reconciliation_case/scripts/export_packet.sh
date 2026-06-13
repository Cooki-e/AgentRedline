#!/bin/sh
set -eu

ROOT=/tmp_workspace/reconciliation_case
RESULTS=/tmp_workspace/results

python3 "$ROOT/tools/reconcile.py"               --invoices "$ROOT/data/invoices.csv"               --purchase-orders "$ROOT/data/purchase_orders.csv"               --policy "$ROOT/policy/reconciliation_rules.csv"               > "$RESULTS/reconciliation_findings.csv"

python3 "$ROOT/tools/reconcile.py"               --invoices "$ROOT/data/invoices.csv"               --purchase-orders "$ROOT/data/purchase_orders.csv"               --policy "$ROOT/policy/reconciliation_rules.csv"               --summary               > "$RESULTS/reconciliation_summary.md"
