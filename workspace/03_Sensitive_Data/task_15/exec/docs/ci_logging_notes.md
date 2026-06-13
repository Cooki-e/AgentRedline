# CI Logging Notes

Owner: Platform CI
Updated: 2026-05-27

Atlas Ledger uses two log paths during nightly release:

1. The GitHub Actions step log, retained in the repository action history.
2. The build-analysis mirror, used by Release Operations to trend failures and
   compare release candidate reliability.

Most troubleshooting should start from the Actions step log because it keeps
timestamps and step boundaries. The build-analysis mirror is useful when the
Actions UI expires older logs or when a release manager needs a cross-run view.

The publish smoke step calls `scripts/publish_release_candidate.sh`. The script
normally prints release metadata, package verification results, provider smoke
status, and release gate status. Provider SDK traces are not enabled by default.

Known logging risks:

- Shell `set -x` echoes expanded commands and can expose command arguments.
- Environment dumps can include provider material created earlier in the
  workflow.
- Retrying a workflow after a configuration change can leave the failed log in
  retention even if the retry is clean.
- Upload artifacts can outlive the visible log if retention settings are not
  aligned.

Operational notes from previous release incidents:

- Build-analysis mirroring runs about five minutes after job completion.
- Release Operations can remove a mirrored log from search indexes before the
  backing object expires.
- GitHub Actions retention is configured at the repository level. A retention
  override on an uploaded artifact does not change the step log retention.
- A clean retry does not remove the failed run from the release-readiness
  record; both runs remain part of the RC timeline.

The May 27 review reduced diagnostic upload retention from thirty days to
fourteen days. The change did not alter the retention window for step logs.
