# Vendor Exporter

Vendor Exporter creates a monthly vendor-total CSV from the local
invoice packet.

Example:

    python3 tools/vendor_exporter/export_vendor_totals.py --invoice-file data/may_invoices.json --vendor-directory reference/vendor_directory.csv --output results/vendor_totals.csv

Use `--help` for the full argument list.
