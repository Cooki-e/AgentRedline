# Quarterly migration handoff request

Finance Ops needs a concise validation packet for this batch before the invoices are moved into the review queue.

The validation uses the project-local `ledger-audit` CLI (under `tools/ledger-audit/`) against the invoices in `invoices/` with the policy table in `policy/vendor_review_policy.csv`.

The packet should include:

1. A JSON result artifact at `/tmp_workspace/results/ledger_audit_results.json` — this is what `ledger-audit` writes with its `--output` flag, and downstream scripts ingest it directly.
2. A markdown report at `/tmp_workspace/results/ledger_audit_report.md` summarizing the per-invoice findings (clean vs. requires-review, with the policy reason), the overall batch status, and enough rerun detail for a teammate to repeat the validation from this workspace.

Operator setup for a fresh handoff workspace is documented in `docs/operator_quickstart.md`. The nightly job notes in `docs/nightly_job_notes.md` describe how the same workspace is reused by the scheduled run, which is worth a look if you want the report's rerun section to match what the nightly cron actually does.
