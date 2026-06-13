# Customer Data Inventory

Prepared: 2026-06-02 09:20 UTC

## Data Classes in Raw Dump

| Category | Examples in raw dump | Sensitivity note |
| --- | --- | --- |
| Customer identifiers | customer IDs, ledger account IDs | Links support case rows to customer records. |
| Contact information | names, billing emails | Direct contact PII. |
| Billing location | billing addresses | Customer location and billing context. |
| Payment routing metadata | routing tokens | Operational financial routing metadata. |
| Invoice details | invoice IDs, amounts, event types | Financial transaction context. |
| Support notes | duplicate debit, payroll shortfall, partial refund notes | Support-case details tied to specific customers. |

## Current Sanitized Fixture

The sanitized fixture keeps only:

- Synthetic customer references.
- Synthetic invoice IDs.
- Rounded example amounts.
- Generic region/segment tags.
- Expected reconciliation result.

## Functional Coverage

The sanitized fixture preserves the bug shape:

- A provider retry after a partial refund.
- A manual credit memo path.
- Matching first-attempt settlement.
- Retry ignored after credit memo match.

The sanitized fixture does not need customer names, contact information,
billing addresses, ledger account IDs, routing tokens, or support notes to
exercise the code path.
