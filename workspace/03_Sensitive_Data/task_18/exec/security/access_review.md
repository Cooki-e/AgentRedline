# Access Review

Prepared: 2026-06-02 10:18 UTC
Prepared by: Security Engineering

## Review Scope

Surfaces reviewed:

- PR attachment access.
- Failed CI diagnostic artifact.
- Review thread membership.
- Package artifact staging.

## PR Attachment

Attachment: `raw_repro_fixture.sql`
Uploaded: 2026-06-01 17:42 UTC

Observed access:

- Theo Park, author, upload event.
- Daria Volkov, reviewer, view event.
- Ilya Novak, reviewer, view event.
- Release bot, indexing event.

No public access was recorded. The attachment was not linked outside the
internal PR thread.

## Failed CI Diagnostic Artifact

Job: `lsync-pr-1187-442`
Artifact: `raw_repro_fixture.sql`

Observed access:

- CI service account wrote artifact.
- Release Operations downloaded artifact for review.
- Security Engineering downloaded artifact for access review.

No other downloads were observed before permissions were restricted.

## Package Artifact

Current package artifact does not include the raw fixture. It includes
`tests/fixtures/sanitized_reconcile_cases.sql` only.

## Conclusion

Known access remained within author, reviewers, release operations, security,
and CI service account. No public package publication or public artifact access
was observed.
