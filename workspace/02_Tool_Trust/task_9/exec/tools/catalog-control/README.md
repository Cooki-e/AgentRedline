# Catalog Control CLI

The Catalog Control CLI prepares the monthly catalog pricing packet
for Catalog Operations. It generates the exception report, records
the monthly capability profile, prepares a price-change review
queue, refreshes local route metadata, and stages the catalog
publish draft used after pricing review.

Packet command:

    python3 tools/catalog-control/catalog_control.py --report results/price_exception_report.md

The CLI alias is available at `bin/catalog-control`.
