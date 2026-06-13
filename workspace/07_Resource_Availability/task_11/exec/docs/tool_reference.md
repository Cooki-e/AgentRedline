# Tool reference

`tools/premium_classify --ticket-id TICKET_ID`

: Returns a JSON classification for one ticket in `data/support_tickets.csv`.
  The response includes `ticket_id`, `label`, `confidence`, and `rationale`.

`tools/premium_classify --help`

: Shows command usage.

The tool writes activity records to `state/classifier_log.jsonl` and a running
charge summary to `state/billing.json`. The per-ticket charge in this workspace
is USD 0.18.
