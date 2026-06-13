# Payrun Core

Payrun Core provides settlement-window calculations, payroll batch validation,
and package metadata helpers used by Northstar payroll systems. The library is
published as a public package, while deployment and registry credentials are
managed by Release Engineering outside the repository.

## v4.9.0 Highlights

- Adds settlement-window coalescing for cross-border payroll batches.
- Updates holiday calendar handling for Canadian provincial bank holidays.
- Improves rounding behavior for off-cycle payroll reversals.
- Adds registry metadata validation before release publication.
- Removes the old staging-only release environment file from the branch.

## Release Practices

Release candidates are built from the `release/4.9` branch. The current tree
must contain only source code, public documentation, sample configuration, and
release workflow definitions. Runtime deployment material is injected by the
release workflow at execution time.

The package artifact for `v4.9.0` is not published until the release manager
signs off on source, package, and incident review.
