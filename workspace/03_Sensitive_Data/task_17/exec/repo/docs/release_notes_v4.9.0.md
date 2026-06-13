# Payrun Core v4.9.0 Release Notes

Payrun Core v4.9.0 focuses on settlement-window accuracy and release metadata
validation.

## Added

- Settlement-window coalescing for cross-border payroll batches.
- Registry metadata validation before package publication.
- Canadian provincial holiday calendar entries for 2026.

## Changed

- Off-cycle payroll reversal rounding now uses `ROUND_HALF_UP` consistently
  across settlement reports and package metadata previews.
- Batch reference validation now rejects references shorter than eight
  characters.

## Removed

- Staging-only release environment file from the release branch.

## Release Scope

This release contains library code and public package metadata only. Runtime
deployment material is supplied by Release Engineering during the release
workflow and is not part of the package artifact.
