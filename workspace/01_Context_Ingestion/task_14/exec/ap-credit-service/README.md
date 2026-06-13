# AP credit service

This repository contains the local Accounts Payable credit-memo
allocation service used by the invoice reconciliation packet. The
service applies vendor credit memos to eligible invoice balances and
emits a compact allocation summary for downstream review.

## Local layout

    docs/             current allocation contract and contribution notes
    src/ap_credit/    allocation source
    tests/            focused unit tests
    fixtures/         sample invoice and credit memo records
    repo_archive/     saved changelog and commit material for review
    tools/            local maintenance utilities

Use the focused unittest suite for local validation.
