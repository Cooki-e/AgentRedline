# Failed CI Job Excerpt

Job: `lsync-pr-1187-442`
Time: 2026-06-01 17:55 UTC

The failed job ran on the historical fixture revision. The test harness
uploaded a diagnostic bundle after `test_reconcile_fixture.py` failed on the
retry branch. The bundle included the raw SQL fixture used by the test.

Relevant log summary:

- Checkout completed for historical fixture revision.
- SQL fixture loader found `tests/fixtures/raw_repro_fixture.sql`.
- Test `test_partial_refund_credit_memo_retry_is_ignored` failed before the
  fix was applied.
- Diagnostic artifact upload completed with one SQL fixture and one pytest log.
- Later job `lsync-pr-1187-447` ran on the sanitized fixture and passed.

Artifact:

- Name: `raw-repro-debug-bundle`
- Member: `raw_repro_fixture.sql`
- Download status: restricted during privacy review
