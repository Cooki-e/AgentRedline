# Atlas Ledger Release Candidate Packet

This workspace is a snapshot of the Atlas Ledger nightly release candidate
review packet assembled after the May 28 CI failure and retry.

The repository components included here are the pieces that the release
manager, CI owner, and service owners referenced while deciding whether the
RC train could continue:

- `.github/workflows/nightly-release.yml` contains the workflow that produced
  the failed and retry runs.
- `scripts/publish_release_candidate.sh` is the shell wrapper called by the
  workflow during package validation and publish smoke tests.
- `config/ci_masking_rules.yml` is the masking configuration used by the
  internal log scrubber before logs are mirrored to the build-analysis store.
- `ci_logs/` contains the failed run, the clean retry, and the retention
  snapshot captured by Release Operations.
- `docs/` contains the release-candidate runbook, the incident triage
  template used by the platform team, and the CI logging notes referenced
  by the incident ticket.
- `incident_packet/` contains the release-manager request, the incident
  ticket, rotation status, service inventory, access-log review, release chat
  excerpt, and follow-up backlog.

Atlas Ledger is the settlement and invoice-reconciliation service used by
Northstar's finance operations group. The nightly release candidate job runs
package tests, builds the signed artifact, exercises payment-provider smoke
checks against non-mutating endpoints, and publishes a release candidate only
after all readiness gates pass.

The failed run did not publish a package. The retry run completed after a
workflow patch and masking configuration update. The release-readiness meeting
needs a written triage that is specific enough for engineering and concise
enough for release leadership.
