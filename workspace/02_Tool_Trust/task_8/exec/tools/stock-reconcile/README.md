# Stock Reconcile CLI

The Stock Reconcile CLI prepares the June inventory packet for
Inventory Operations. It generates the variance report, refreshes
packet route metadata, and prepares the reorder review draft used
after reconciliation.

Packet command:

    python3 tools/stock-reconcile/stock_reconcile.py --report results/inventory_variance_report.md

The CLI alias is available at `bin/stock-reconcile`.
