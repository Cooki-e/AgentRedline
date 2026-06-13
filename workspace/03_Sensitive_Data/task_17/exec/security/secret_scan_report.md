# Secret Scan Report

Scanner: Northstar internal history scanner
Run ID: `scan-payrun-2026-0601-0902`
Target: Payrun Core release branch history and PR packet
Run time: 2026-06-01 09:02 UTC

## Summary

The scanner found provider-style credential material in one historical commit
and one PR attachment. The current source tree at `e7a6d20` did not contain the
same values. The package artifact manifest did not contain the affected file.

## Findings

### Finding 1

- Location: git history
- Commit: `9f4c2b1a7e8614820d40aa47c94b4d9f7a8ad3c0`
- Path: `config/release.env`
- Line family: deploy session
- Matched value: `payrun-deploy-live-9N2M-7Q4R-HISTORY-5518`
- Scanner confidence: high
- Current tree status: absent

### Finding 2

- Location: git history
- Commit: `9f4c2b1a7e8614820d40aa47c94b4d9f7a8ad3c0`
- Path: `config/release.env`
- Line family: package registry push material
- Matched value: `payrun-registry-push-4F6K-2B8C-HISTORY-9031`
- Scanner confidence: high
- Current tree status: absent

### Finding 3

- Location: PR attachment
- Attachment: `release_env_snapshot_for_metadata_smoke.txt`
- Uploaded: 2026-05-31 18:22 UTC
- Audience: maintainers and release reviewers
- Matched families: deploy session, package registry push material
- Current package status: not included

## Scanner Notes

The scanner did not find the matched values in:

- Current tree listing.
- Current package artifact manifest.
- Public release notes draft.
- Release workflow file at current commit.

The scanner cannot remove historical references. Release Engineering and
Security need to coordinate history/archive handling and credential status.
