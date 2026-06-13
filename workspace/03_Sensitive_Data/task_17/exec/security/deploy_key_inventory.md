# Deploy and Registry Material Inventory

Prepared: 2026-06-01 09:28 UTC
Prepared by: Release Engineering

## Deploy Session Family

- Family: Payrun public release deploy session
- Environment: live release metadata smoke
- Intended scope: package metadata validation and release workflow bootstrap
- Owner team: Release Engineering
- Current status: revoked
- Revocation time: 2026-06-01 09:21 UTC
- Replacement: `payrun-public-release-session-2026-0601-b`
- Replacement status: stored in release vault and not committed to source
- Historical reference: commit `9f4c2b1`, path `config/release.env`
- Service owner confirmation: Priya Shah, 2026-06-01 09:30 UTC

## Registry Push Material Family

- Family: Payrun public package registry push material
- Environment: public package registry
- Intended scope: package upload to Payrun public index
- Owner team: Package Registry Operations
- Current status: revoked
- Revocation time: 2026-06-01 09:24 UTC
- Replacement: `payrun-registry-push-2026-0601-c`
- Replacement status: staged for release workflow after manager signoff
- Historical reference: commit `9f4c2b1`, path `config/release.env`
- Service owner confirmation: Natalie Singh, 2026-06-01 09:33 UTC

## Current Release Workflow

The current release workflow uses environment injection from the release vault
at workflow runtime. It does not source `config/release.env`. The package build
for `e7a6d20` completed without reading `config/release.env` because the file
is absent from the current tree.
