# Incident Ticket: CI-2026-0528-1842

Status: Containment in progress
Opened: 2026-05-28 02:58 UTC
Opened by: Mara Feld, Platform CI
Severity: SEV-3 release process incident
Service: Atlas Ledger nightly release candidate

## Summary

The `nightly-release` workflow for Atlas Ledger run 1842 printed provider
environment material during the `Provider publish smoke` step. The job failed
after provider smoke because the release gate required a manual SBOM-delta
approval. The package upload step was skipped.

The retry run 1843 used commit `1cf8b90`, removed the provider environment
dump from the script path, added provider material masking, and passed the dry
run release gate with the SBOM delta approval ID.

## Detection

Release Operations noticed the environment dump while comparing run 1842 and
run 1843 for the release manager. The build-analysis mirror had already
ingested run 1842 stdout by the time the ticket was opened.

## Known Exposure Surface

- GitHub Actions step log for run 1842.
- Build-analysis mirror object for run 1842 stdout.
- Release Operations Slack discussion that referenced the affected line range
  but did not paste the values.
- This incident ticket.

No uploaded diagnostics file contained provider material. The diagnostic
artifact contains `dist/sbom.json`, `build/release-metadata.json`, and
`build/provider-smoke-summary.json`.

## Current Assessment

- Failed run did not publish an RC package.
- Provider smoke calls completed against read-only endpoints.
- Payments connector material had a longer validity window than the failed job.
- Orbital client assertion had a short validity window and expired before the
  ticket was opened.
- Masking rules did not cover provider names that lacked the usual generic
  credential words.
- Shell tracing and environment dumping were re-enabled in commit `6d03e62`
  while debugging a staging provider bootstrap issue.

## Owner Notes

Payments owner Omar Sato started rotation at 03:00 UTC. Orbital owner Devika
Rao confirmed that the assertion class used by the smoke job is one-time
scoped to environment metadata and reconciliation schema checks. Security
Engineering asked for access-log review before the release manager moves the
RC from conditional continue to continue.
