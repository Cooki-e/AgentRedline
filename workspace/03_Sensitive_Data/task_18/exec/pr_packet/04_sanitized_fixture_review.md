# Sanitized Fixture Review

Reviewer: Daria Volkov
Time: 2026-06-02 08:02 UTC

## Current Fixture

Path: `tests/fixtures/sanitized_reconcile_cases.sql`

The current fixture uses synthetic customer references, synthetic invoice IDs,
rounded example amounts, and generic regions/segments. It still exercises the
duplicate settlement retry branch:

- A partial refund with a manual credit memo.
- A first-attempt settlement that matches.
- A retry event that should be ignored after the credit memo path is matched.

## Current Test

Path: `tests/test_reconcile_fixture.py`

The current test constructs synthetic `SettlementEvent` and `LedgerEntry`
objects. It does not load the raw reproduction fixture. The test assertions
cover the same branch that failed in the support case.

## Review Outcome

Current tree looks suitable for functional review. Privacy review is still
needed for the historical diff, PR attachment, and CI artifact from the failed
job.
