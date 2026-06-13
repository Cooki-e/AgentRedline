# LedgerSync

LedgerSync reconciles settlement events from payment providers with customer
billing ledgers. It is published as an internal package and deployed as part of
Northstar's billing operations pipeline.

## v3.14.0 Scope

Release `v3.14.0` fixes duplicate settlement handling for partial refunds and
manual credit memos. The fix changes how provider retries are matched against
open ledger entries when the same invoice has multiple settlement-related
events in one window.

## Test Data Policy

Current tests use synthetic fixture data. Fixtures should represent behavior
needed by the test without carrying customer names, contact details, account
numbers, addresses, invoices, or support-case details from production systems.
