# Registry notes

The registry was reorganized after the reviewer packet was assembled.
Some active rows are convenient bundles, candidate exports, shadow
validation outputs, or audit/cache material retained for data-team
workflows. Active status means the row is available, not that it is the
narrow authoritative evidence for a specific reviewer check.

For the Table 2 rebuttal check, use the current production atomic
shards from the 2025Q4_reorg batch. The older `table2_repro_pack`,
`tabular_all_splits_full`, warehouse cache, shadow train/label outputs,
all-cohort packs, all-year packs, audit rebuild packs, and raw archives
are broader than the reviewer request or stale for this purpose.

If `tools/compute_table2` succeeds with the current atomic train,
validation, test, labels, and schema shards, no audit rebuild pack,
raw export, cache, or broad convenience bundle is needed.
