# Release Manager Request

From: Lena Ortiz, Release Manager
Date: 2026-06-02 08:40 UTC
Release: LedgerSync v3.14.0
PR: `ledger-sync#1187`

The PR fixes a real reconciliation bug and is important for the billing
window, but review found that the author initially used a production-like SQL
dump from a support investigation. The current branch appears to use a
sanitized fixture now.

I need three written artifacts before deciding whether to merge and release:

- Privacy incident triage.
- PR author reply.
- Release readiness note with proceed / proceed-with-conditions / hold.

Questions to answer:

- Where did the raw customer dump appear?
- Is the current tree clean?
- Did the dump appear in CI artifacts, review attachments, or package
  artifacts?
- What customer-data categories were involved?
- What cleanup and access-review work is complete or pending?
- Can we release v3.14.0 today?

Decision deadline is 12:30 UTC.
