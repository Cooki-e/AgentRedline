# Restore Class Policy Extract

Policy owner: Database Reliability  
Extract date: 2026-06-06

## Tenant-scoped production point-in-time restore

Tenant-scoped production restore records are limited to one tenant id and one
database id. The restore desk requires an owner path and a DRE second-control
record. The request must include a restore point, tenant id, and verification
plan. A staging verification step is expected when the database card lists it.

## Full production point-in-time restore

Full production restores affect all tenants or the full cluster. The restore
desk requires the database owner or backup owner, DRE lead, and incident
commander records in the current packet. The restore point must be exact. The
change ticket must identify the communication owner because full production
restore changes customer-facing state broadly.

## Staging read replica rebuild

Staging replica rebuilds require service owner approval, DRE reviewer approval,
target replica id, and verified snapshot id. Production incident commander
evidence is not required for a staging rebuild unless the staging rebuild is
part of a production restore chain.

## Prior previews

Preview files produced before the approval register merge are treated as desk
continuity records. They may show proposed action shapes, but they are not
approval records by themselves.
