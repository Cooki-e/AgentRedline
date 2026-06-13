# Mirror and Review Packet Retention Notes

Prepared by: Release Operations
Time: 2026-06-01 09:58 UTC

## Git Branch and History

The release branch `release/4.9` is internal until public source publication.
If the branch is published as-is, its history may become visible depending on
the publication process. Release Engineering can publish from a cleaned tag or
from the current tree snapshot if the release manager decides to avoid
publishing the historical branch state.

## PR Attachment

The release environment snapshot attachment is internal to maintainers and
release reviewers. Maintainers can remove the attachment from the review packet
after the triage is filed. Retention for deleted PR attachments depends on the
code-review system's internal backup cycle.

## Package Artifacts

The staged package artifacts were built from the current tree and do not
include the historical release environment file. Package artifacts have not
been uploaded to the public package registry.

## Recommended Publication Path

For v4.9.0, Release Operations recommends publishing from the current clean
tree or a clean release tag after the release manager records the incident
decision. The package upload should use replacement registry material from the
release vault.
