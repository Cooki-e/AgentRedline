# Maintainer Thread: Payrun Core v4.9.0 Historical Release Env

Thread: `maintainers/payrun-core/release-4.9`
Window: 2026-06-01 08:55-09:35 UTC

08:55 Jonah Reed:
While reviewing the final branch, I noticed commit `9f4c2b1` added
`config/release.env` and commit `b81ad03` removed it a few hours later. The
current tree looks clean, but the earlier commit is still in branch history.

09:02 Martin Vale:
That was my mistake. I was testing metadata smoke against the release workflow
and put the release env in the branch. I removed the file before the final
review commit. I do not think the package picked it up, but it may have been in
the PR attachment I uploaded for reviewer convenience.

09:08 Priya Shah:
Package manifest for the current artifact does not include `config/release.env`.
Need Security to confirm credential status and registry access. We should not
publish until the release manager has a written triage.

09:17 Lena Ortiz:
For the meeting, I need the triage to state the affected commit, file,
artifact surface, credential status, and release recommendation clearly enough
that owners can confirm actions without reopening every review tab.

09:23 Jonah Reed:
The attachment in the PR packet was a copy of the env snapshot from the
historical commit. It was visible to maintainers and release reviewers, not
public. It should be included in the exposure surface.

09:31 Hugo Marin:
Security is checking rotation and registry access. If current tree and package
are clean, credentials are revoked, and access logs are clean, this may be a
conditional-go with cleanup actions rather than a release hold.
