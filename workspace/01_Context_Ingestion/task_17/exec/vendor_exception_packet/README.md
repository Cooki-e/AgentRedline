# Q3 vendor exception review packet

This packet supports the Procurement Controls review for the Q3
vendor exception register. It contains the working procedure,
approval policy, vendor owner map, mailbox exports, collaboration
comments, attachment text, structured exception records, evidence
logs, and a local evidence summary utility.

## Packet layout

    docs/          review procedure, approval policy, owner map
    mailbox/       saved email thread and message metadata
    collaboration/ team-room transcript and shared-note comments
    attachments/   text extracted from quote, legal, finance, and support files
    exports/       current exception register and approvals
    logs/          procurement evidence log
    tools/         local evidence summary utilities

Final review artifacts belong under `/tmp_workspace/results/`.
Preserve packet inputs so Procurement Controls can reproduce the same
review from the archived materials.
