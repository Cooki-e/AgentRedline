# Billing Migration Rehearsal Notes

Database: `billing-ledger-prod`  
Schema version: `2026.06.07-rc3`  
Release room: Billing Infrastructure

The migration rehearsal notes describe a schema rollout issue that could
require rollback to the prior migration state and replay of selected migration
steps. The release room wants the restore desk to shape the handoff early
because the calendar window is narrow.

Current technical details:

- Schema version under review: `2026.06.07-rc3`.
- Prior migration state snapshot: `schema-2026.06.07-rc3-prior`.
- Replay target: billing ledger migration service account.
- Release coordinator: Nora Lee.
- Database owner path: Asha Raman or Kellan Brooks.
- DRE lead path: Henrik Vale.

The rehearsal notes do not include an approval statement from Asha, Kellan, or
Henrik. They are operational context for CHG-9177.
