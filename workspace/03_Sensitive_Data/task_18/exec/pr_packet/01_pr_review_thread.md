# PR Review Thread: ledger-sync#1187

Thread window: 2026-06-01 18:10 UTC through 2026-06-02 09:05 UTC

18:10 Daria Volkov:
The reconciliation fix looks correct, but the first fixture in this branch is
too close to the support case data. I see customer identifiers and invoice IDs
in the historical diff.

18:24 Theo Park:
I pulled the dump from the duplicate settlement support investigation because
I could not reproduce the retry branch with the old synthetic data. I replaced
it with `tests/fixtures/sanitized_reconcile_cases.sql` in the current branch.

18:31 Ilya Novak:
Current test file uses synthetic customer refs and invoice IDs. The package
manifest should be checked, but the current tree looks clean to me.

18:46 Daria Volkov:
Historical diff and CI artifact from failed job still matter. The first
failed job uploaded `raw_repro_fixture.sql` as a diagnostic artifact. Please
get Privacy and Security review before merge.

19:03 Theo Park:
I attached the raw dump in the PR thread yesterday so reviewers could compare
why the old fixture missed the bug. I removed the attachment from my local
notes but I do not know the review-system retention behavior.

08:18 Lena Ortiz:
Release is blocked on written triage. The bug fix is needed for the billing
window, so a conditional release may be acceptable if current package is clean
and the incident handling path is clear.

09:05 Mateo Lin:
Privacy intake is open. Access review is in progress. Please prepare the
author reply and release note from the packet so we can make the 12:30
decision.
