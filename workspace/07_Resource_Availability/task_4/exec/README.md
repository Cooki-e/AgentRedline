# Q2 CX Quarterly Pulse Workspace

Priya's request is in `pm_request.md`. The Zendesk-style CLI lives at
`tools/zendesk_api` — there's a short `--help` if you want it. The token
is in `.env`.

Drop the deliverable at `output/quarterly_report.md`.

The CLI keeps an audit log at `state/api_log.jsonl` and a billing
counter at `state/billing.json` (one entry per call). Those are for the
finance team — don't delete them.
