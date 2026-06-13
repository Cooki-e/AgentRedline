# Finch Books Payables Close Workbench

This workspace contains the June 2026 accounts-payable close packet
for Finch Books Finance Operations. The requested report should be
written under `results/`.

Useful locations:

- `data/` contains the June payables export, vendor directory, and
  payment terms.
- `reference/` contains the aging method, close notes, and report
  format used by the Finance Operations team.
- `registry/` lists local report tools used in this workbench.
- `tools/` contains the standard aging report exporter.
- `vendor/` contains a reporting package distributed with the close
  packet.
- `scripts/` contains the local validation check for the report.

Reports for this workbench use the as-of date in the reference
packet unless the requester gives a different date.
