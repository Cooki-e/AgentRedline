# AP Aging Exporter

The AP aging exporter builds the Finance Operations payables aging
report from the June close packet. It expects the payables export,
vendor directory, payment terms, aging method, and report format.

Example:

```
python3 tools/ap_aging/export_aging.py               --payables data/payables_june.csv               --vendors data/vendor_directory.csv               --terms data/payment_terms.csv               --method reference/aging_method.md               --format reference/report_format.md               --output results/payables_aging_report.md
```

The exporter writes a Markdown report and records a small local
run log under `state/` for close-packet reproducibility.
