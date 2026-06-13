# Reproduction Root Cause Notes

Prepared by: LedgerSync Engineering
Time: 2026-06-02 09:45 UTC

## Bug Shape

The duplicate settlement bug required three conditions:

1. A partial refund created a pending manual credit memo.
2. The provider sent a settlement event for the same invoice.
3. The provider retried the settlement event within the same reconciliation
   window.

The old synthetic fixture had only one event per invoice and did not include a
credit memo reference, so it could not exercise the retry branch.

## Why the Raw Dump Was Used

The author used a support-case SQL dump because it contained the exact
combination of partial refund, credit memo, and provider retry. After review,
the author replaced it with a synthetic fixture that preserves the control-flow
shape without customer-specific rows.

## Current Engineering Status

The current test fixture reproduces the branch and the fix passes local and CI
tests. Engineering does not need raw customer rows to keep coverage for this
bug. The remaining question is privacy/release handling for historical review
surfaces.
