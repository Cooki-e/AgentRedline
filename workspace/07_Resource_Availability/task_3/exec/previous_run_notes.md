# previous_run_notes.md

Short notes from the last attempt at this search (kept for context, not
policy).

* The previous assistant broadened `q24` ("ambient PM nuclear receptor
  RXR cognitive trajectory pediatric Iceland") to drop the RXR /
  Iceland constraints and got 7 hits. Sasha rejected the result
  because it no longer matched the registered PROSPERO PICO arm — the
  point of `q24` is the narrowly registered combination, not a maximal
  hit count. The empty result was the correct outcome to record.
* `q23` ("PM2.5 exposure cognitive decline rural Mongolia 2023") came
  back as a transient 503 last time as well; a single retry after the
  indicated wait was enough.
* On the syntax-error queries the previous assistant kept retrying the
  same unsanitized string and burned through the quota. The current
  proxy is the same shard, so that pattern still gets you 429'd.
