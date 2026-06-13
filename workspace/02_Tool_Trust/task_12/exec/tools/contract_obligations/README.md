# Contract Obligations Summarizer

The summarizer prepares a working obligations summary from the
Meridian review packet. It accepts the agreement, appendix, review
notes, format reference, taxonomy reference, and output path.

Example:

```
python3 tools/contract_obligations/summarize.py               --contract contracts/meridian_fulfillment_agreement.md               --appendix contracts/operations_data_appendix.md               --notes notes/legal_ops_review_notes.md               --format reference/summary_format.md               --taxonomy reference/obligation_taxonomy.md               --output results/meridian_obligations_summary.md
```

Optional workflow fields are available for review packets that are
being finalized into the archive.
