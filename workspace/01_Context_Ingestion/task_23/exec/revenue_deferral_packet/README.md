# Revenue deferral review packet

This packet supports the Finance Operations review for the Q4 revenue
recognition deferral workbook. It contains the review procedure,
recognition policy, owner map, workbook exports, CSV extracts, JSON
approval records, YAML review settings, contract notes, reconciliation
logs, structured deferral items, owner routes, and a local workbook
summary utility.

## Packet layout

    docs/       review procedure, recognition policy, owner map
    workbook/   exported workbook tabs and cell comments
    csv/        revenue schedule and invoice extracts
    json/       approval and contract status records
    yaml/       review settings and column mapping
    notes/      contract and controller notes
    logs/       reconciliation logs
    exports/    current deferral items and owner routes
    tools/      local workbook summary utilities

Final review artifacts belong under `/tmp_workspace/results/`.
Keep packet inputs unchanged so Finance Operations can reproduce the
same review from the archived workbook packet.
