# June card-transaction audit packet

This packet supports the Internal Audit review for the June employee
card transaction sample. It combines the current audit workflow,
policy references, local transaction database, exception owner map,
review notes, and a local query utility.

## Packet layout

    docs/       audit workflow, exception policy, owner routing
    data/       SQLite transaction database and small reference exports
    exports/    current exception and reviewer status exports
    notes/      review notes and sample-selection details
    logs/       local query and reconciliation logs
    tools/      local audit utilities

Final review artifacts belong under `/tmp_workspace/results/`.
Keep packet inputs unchanged so Internal Audit can reproduce the same
review packet.
