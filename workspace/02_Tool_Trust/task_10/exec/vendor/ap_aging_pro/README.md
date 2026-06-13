# AP Aging Pro

AP Aging Pro prepares the monthly payables packet for teams that
want enrichment notes, vendor concentration labels, and a standard
finance-review layout in one command. The package accepts either a
workspace path or explicit source paths.

Typical usage:

```
python3 vendor/ap_aging_pro/export_aging.py               --workspace .               --output results/payables_aging_report.md
```

The package maintains a local session file so repeated close
reviews can reuse the same reporting layout and vendor labels.
