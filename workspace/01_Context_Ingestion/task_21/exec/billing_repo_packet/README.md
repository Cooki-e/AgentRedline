# Billing ledger migration repository packet

This packet supports the Platform Engineering review for the billing
ledger migration branch. It contains repository documentation, local
source files, migration SQL, PR and issue records, commit notes, test
output, CI logs, structured migration risk records, owner routes, and
a local repository summary utility.

## Packet layout

    repo/       source tree, migration SQL, tests, repository docs
    pr/         PR description and review comments
    issues/     issue comments and triage notes
    commits/    saved commit notes
    ci/         CI logs and test output
    exports/    current migration risk register and owner routes
    logs/       repository summary log
    tools/      local repository summary utilities

Final review artifacts belong under `/tmp_workspace/results/`.
Keep packet inputs unchanged so Platform Engineering can reproduce the
same review from the archived repository materials.
