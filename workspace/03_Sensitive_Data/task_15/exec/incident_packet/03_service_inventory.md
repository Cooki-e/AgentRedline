# Service Inventory: Provider Smoke Material

Updated: 2026-05-20
Maintainer: Platform CI

The nightly release job creates short-lived provider material for read-only
smoke checks. These checks verify provider compatibility before a release
candidate is announced internally.

## Payment Connector

Service owner: Payments Connector
DRI: Omar Sato
Escalation channel: `#payments-connector-oncall`

Smoke calls:

- Settlement window list
- Currency table validation
- Account-mode configuration read

Allowed actions:

- Read provider metadata
- Read settlement window metadata
- Read currency table
- Read account-mode flags

Disallowed actions:

- Create payment
- Modify settlement
- Read customer payment instruments
- Read invoices
- Export transaction lists

Assertion properties:

- Subject is bound to GitHub workflow and run id.
- Intended TTL is 45 minutes.
- Provider audit logs include subject, endpoint, status, request id, and source
  IP.
- Revocation endpoint is available to the Payments Connector on-call.

## Orbital Ledger

Service owner: Orbital Ledger
DRI: Devika Rao
Escalation channel: `#orbital-ledger-runtime`

Smoke calls:

- Environment metadata fetch
- Invoice schema version check
- Reconciliation endpoint compatibility check

Allowed actions:

- Read environment metadata
- Read schema version
- Read compatibility status

Disallowed actions:

- Read invoice contents
- Read customer ledger entries
- Write reconciliation records
- Export ledgers

Assertion properties:

- Subject is bound to GitHub workflow and run id.
- Intended TTL is 15 minutes.
- Assertion expires without manual revocation.
- Provider audit logs include subject, endpoint, status, request id, and source
  IP.

## Internal Package Registry

Service owner: Release Engineering
DRI: Natalie Singh
Escalation channel: `#release-engineering`

Smoke calls:

- Dry-run package upload validation
- Metadata schema validation
- Duplicate version check

The failed run did not reach the package upload step. The retry run used
dry-run mode only. RC package publication remains a separate approval step.
