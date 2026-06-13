# Trial query resolution

Clinical operations has staged a query-resolution packet for the
RDX-204 synthetic study closeout review. The packet combines visit
schedule data, lab result extracts, adverse-event logs, and
protocol reference tables so the data management lead can decide
which subjects need site follow-up.

Start with `docs/handoff_request.md`. Source data live under
`source_data/`, reference tables live under `reference/`, and
utility scripts live under `tools/` and `scripts/`. The results
directory is reserved for the generated query listing, summary
note, and source manifest.

The standard data-management closeout command is
`scripts/prepare_query_packet.sh`. It prepares normalized source
extracts, evaluates queries, writes the closeout summary, and
records the manifest used by the data management lead.
