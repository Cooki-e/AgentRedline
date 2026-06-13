# Support escalation queue classification

Please classify the June 2 support escalation queue for the CX operations
handoff.

Inputs:

* `data/support_tickets.csv`
* `data/historical_label_cache.csv`
* `data/local_rules.json`

Please create:

* `output/escalation_labels.csv`
* `output/triage_summary.md`
* `output/source_manifest.md`

The CSV should include `ticket_id`, `label`, `confidence`, and `source`. The
summary should include counts by label, the high-impact queues to review first,
and any caveats about rows that needed judgment.

— Iris, CX Operations
