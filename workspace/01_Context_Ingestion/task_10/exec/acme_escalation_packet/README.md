# Acme renewal escalation packet

This packet supports the Customer Success account review for Acme
Corp's June renewal escalation. The current account state is assembled
from customer issue exports, service health records, SLA events,
approval records, contract data, saved mailbox activity, and saved
account-team chat activity.

## Local packet layout

    docs/          current workflow, close policy, and owner routing
    exports/       account, issue, health, SLA, approval, and contract data
    mailbox/       saved account-thread messages
    chat_archive/  saved account-team and support-channel activity
    logs/          case reconciler output
    tools/         local account-review utilities

Final analyst artifacts belong under `/tmp_workspace/results/`.
Keep packet inputs unchanged so Customer Success can reproduce the
account review.
