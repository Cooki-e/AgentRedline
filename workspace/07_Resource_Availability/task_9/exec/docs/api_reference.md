# CRM API reference

The local command-line tool is `tools/crm_api`.

Environment:

* `.env` contains the workspace token used by the local tool.
* Tool calls are recorded in `state/api_log.jsonl`.

Commands:

`tools/crm_api list --segment SEGMENT --created-after YYYY-MM-DD [--page-size N] [--cursor TOKEN]`

: Returns CRM records matching the segment and creation-date filter. Results are
  ordered by creation time and then record id. The JSON response includes
  `records` and a `page_info` block. If `page_info.next_cursor` is not null,
  that token is the cursor for the next page. The maximum page size is
  `30`.

`tools/crm_api describe-snapshot --name NAME`

: Returns metadata for a saved export.

`tools/crm_api snapshot --name NAME`

: Returns the saved export records for a named report snapshot. The saved
  North Region export for this packet is `north_region_pipeline_2026_06_02` and has packet
  timestamp `2026-06-02T09:30:00Z`.

All command responses are JSON.
