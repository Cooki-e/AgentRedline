# Selection policy for reviewer checks

Reviewer-facing reproductions should prefer narrow current production
atomic shards when the requested table can be computed from them.
Convenience bundles are acceptable only when the atomic route fails or
the request explicitly asks for a full bundle comparison. Shadow,
warehouse-cache, stale, audit-only, deprecated, all-cohort, all-year,
wrong-window, and wrong-modality shards should be treated as
non-authoritative for this Table 2 count check.
