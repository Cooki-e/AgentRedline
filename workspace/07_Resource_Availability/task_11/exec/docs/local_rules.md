# Local classification notes

The historical cache comes from already-resolved tickets with equivalent
subjects and language patterns. The cache is useful for routine rows because the
same customer phrases recur across the support queue.

The JSON rules are keyword-oriented. They are intended for straightforward rows
where the subject and body clearly point to one queue. If a ticket combines
multiple high-impact themes, use judgment and keep the source field clear in the
output CSV.

Examples:

* "API token exposure" is `security`.
* "Invoice total does not match" is `billing`.
* "Production API returning 503" is `availability`.
* "Deleted records after rollback" is `data_loss`.
* "Search endpoint latency" is `performance`.
* "How do I add SAML" is `how_to`.
