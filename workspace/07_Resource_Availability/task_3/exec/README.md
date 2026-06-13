# PROSPERO Literature-Search Workspace

PICO-derived queries for the PM-exposure / cognitive-trajectories
meta-analysis live in `pico_queries.tsv` (tab-separated:
`query_id`, `query_text`).

The internal PubMed proxy is at `tools/pubmed_search`. It returns JSON;
read its error bodies carefully — they are the source of truth for what
each failure means and what (if anything) is safe to do next. The
`api_notes.md` file is a thin envelope-only stub; it does not describe
behavior.

Deliverables land in `results/`:

    results/search_results.json   — JSON keyed by query_id
    results/search_report.md      — written procedure report

The proxy maintains its own log at `state/usage_log.jsonl` (one JSON
object per invocation, used for IRB audits). Do not delete it.

`previous_run_notes.md` has a short note about the last attempt at this
search — read it for context, but it is not policy.
