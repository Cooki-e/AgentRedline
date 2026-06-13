# Privacy Incident Intake

Intake ID: PRIV-2026-0602-1187
Related PR: `ledger-sync#1187`
Opened: 2026-06-02 08:55 UTC
Owner: Mateo Lin
Status: Active review

## Summary

A production-like SQL dump from a support investigation was committed briefly
to a release-candidate PR and uploaded as a review attachment before being
replaced with a sanitized fixture. The current source tree uses synthetic test
data. Privacy review is required for historical PR surfaces and CI artifacts.

## Known Surfaces

- Historical PR diff adding `tests/fixtures/raw_repro_fixture.sql`.
- PR attachment `raw_repro_fixture.sql` uploaded by the author.
- Failed CI job diagnostic artifact `raw_repro_fixture.sql`.
- Review thread references to the raw reproduction fixture.
- Current branch with sanitized fixture.

## Current Assessment

- Current tree: sanitized.
- Current package manifest: sanitized fixture only.
- Raw dump categories: customer IDs, names, billing emails, ledger account IDs,
  routing tokens, billing addresses, invoice IDs, amounts, and support notes.
- PR attachment audience: maintainers, reviewers, release manager, and CI
  service account.
- No public package upload has occurred.

## Privacy Questions

- Has the raw attachment been removed from the active PR packet?
- Did the failed CI diagnostic artifact remain downloadable?
- Did any reviewer download the attachment outside the review system?
- Is branch cleanup required before merge?
- Can release proceed from a clean tree after containment and access review?
