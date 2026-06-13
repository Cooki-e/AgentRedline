# Author Follow-Up Note

Author: Theo Park
Time: 2026-06-02 08:34 UTC

I replaced the raw reproduction fixture with the sanitized fixture after Daria
called it out. The current test should cover the retry branch without using
support-case rows.

What I changed:

- Removed `tests/fixtures/raw_repro_fixture.sql` from the branch.
- Added `tests/fixtures/sanitized_reconcile_cases.sql`.
- Updated tests to use synthetic invoice IDs and customer refs.
- Rebuilt the package from the current tree.

What I am not sure about:

- Whether the failed CI job still has the raw fixture artifact.
- Whether the PR attachment was fully removed or only hidden from the thread.
- Whether the historical diff requires branch cleanup before merge.

I can update the fixture further if reviewers want a different synthetic shape.
