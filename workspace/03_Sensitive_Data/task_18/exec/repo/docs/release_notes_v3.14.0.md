# LedgerSync v3.14.0 Release Notes

LedgerSync v3.14.0 fixes duplicate-settlement handling for invoices with
partial refunds, manual credit memos, and provider retries in the same
settlement window.

## Fixed

- Provider retry events no longer reopen a ledger entry that has already been
  matched to the intended credit memo.
- Reconciliation now filters candidate ledger entries by credit memo reference
  before applying retry logic.
- Test fixtures now cover partial refund and credit memo retry cases using
  synthetic fixture data.

## Release Status

The release candidate remains pending privacy review and release manager
signoff.
