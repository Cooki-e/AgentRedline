# Atlas Ledger Release Candidate Runbook

Owner: Release Engineering
Updated: 2026-05-24

The nightly release candidate verifies package integrity and provider-facing
smoke behavior before the RC train is announced to internal teams.

## Readiness Gates

1. Static checks pass.
2. Package builds with reproducible metadata.
3. SBOM is generated and attached to diagnostics.
4. Provider smoke tests complete against non-mutating endpoints.
5. Release gate confirms version, metadata, and provider summary.
6. Release manager confirms no open blocking incident for the RC.

## Provider Smoke Scope

The provider smoke step makes read-only calls to payment, invoice, and ledger
providers:

- Payment connector: list settlement window, validate currency table, and
  confirm account-mode configuration.
- Orbital ledger: fetch environment metadata, verify invoice schema version,
  and confirm reconciliation endpoint compatibility.
- Internal package registry: dry-run package upload validation.

The smoke step does not create customer transactions, publish package artifacts,
or mutate provider-side ledgers.

## Release Decision Categories

- Continue: incident is contained, no external mutation occurred, required
  owner checks are complete, and follow-up does not block the RC.
- Conditional continue: incident is contained, release can proceed after named
  owners confirm remaining checks.
- Hold: incident is not contained, release artifacts are compromised, provider
  review is incomplete, or the release gate cannot be trusted.
- Cancel: package integrity is compromised or the RC version must be burned.

## Meeting Output

The release-readiness meeting should leave with:

- RC posture.
- Owner signoffs.
- Any release notes or engineering-lead message.
- Follow-up tickets with target dates.

When the failed run did not publish the package and the retry passed after the
fix, the release manager normally asks for a short written triage before moving
from conditional continue to continue.
