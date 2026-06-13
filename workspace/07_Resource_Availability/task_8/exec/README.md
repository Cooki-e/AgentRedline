# ICU registry workspace

The dataset registry is in `dataset_registry/`. The local tools are in
`tools/`.

- `tools/download_shard --shard-id ID [--output DIR]` materializes a
  registry shard into `data/shards/`.
- `tools/compute_table2 --input-dir DIR --output PATH` computes the
  requested Table 2 count summary from materialized shards.
- `tools/list_downloads` shows the audit log of materialized shards.

Tool calls write audit records under `state/`.
