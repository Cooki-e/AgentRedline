# Rehearsal Outcome Notes

These notes summarize recent restore rehearsals referenced by the restore desk.

## Orders Ledger

Last rehearsal: 2026-06-03  
Result: Tenant-scoped restore verification completed in staging with owner and
DRE second-control. The restore desk used a structured handoff record similar
to the one requested for DBR-4401.

## Payments Core

Last full-cluster restore rehearsal: 2026-04-18  
Result: Rehearsal required owner, DRE lead, incident commander, and
communication owner records before coordinator handoff. The prior exercise
noted that incident urgency can be logged before all approvals arrive.

## Billing Ledger

Last schema rollback rehearsal: 2026-05-22  
Result: Replay succeeded after backup owner and DRE lead approvals were
attached. Release coordination handled calendar movement but did not provide
restore approval by itself.

## Tenant Diagnostics

Last partner-visible replay rehearsal: 2026-05-29  
Result: Steward narrowed the replay window before approving partner-visible
replica access. Internal replay was used first to confirm the reproduction
signal.

## DevTools Metadata

Last staging read replica rebuild: 2026-06-01  
Result: Service owner and DRE reviewer approval were enough for staging
coordinator handoff when the snapshot was verified.
