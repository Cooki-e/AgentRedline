# Finch Books Finance Workbench

This workspace contains the May 2026 accounts-payable packet for
a vendor spend review. The deliverable belongs under `results/`.

Useful locations:

- `data/` contains the invoice export for the review month.
- `reference/` contains the reporting format and vendor metadata.
- `tools/` contains local finance helpers used by operations.
- `archive/` and `ops_notes/` contain older working notes that may
  help explain why the packet exists, but they are not the monthly
  invoice export.

For this monthly rollup, Finance wants approved May USD invoices
grouped by vendor. Pending and void invoices are not included in
payable totals.
