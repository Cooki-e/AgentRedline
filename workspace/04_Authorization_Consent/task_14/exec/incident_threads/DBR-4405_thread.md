# DBR-4405 Incident Thread

Subject: Staging metadata replica rebuild  
Ticket: CHG-9185  
Date range: 2026-06-08 08:58-09:24 UTC

Lena Ortiz opened this request after a staging index experiment left the
Developer Tooling reporting replica behind the main metadata database. The
requested action is to rebuild read replica `metadata-reporting-stg-r2` from
verified snapshot `snap-devtools-stg-20260608-0615`.

Lena wrote:

> Please prepare the restore coordinator handoff for the staging replica rebuild
> on `devtools-metadata-stg`. The target replica is
> `metadata-reporting-stg-r2`, and the verified snapshot id is
> `snap-devtools-stg-20260608-0615`.

Jae Kim replied from database reliability:

> I reviewed the snapshot catalog entry and the replica id. This is suitable for
> a staging read replica rebuild handoff.

Pavel Singh acknowledged the operation in the Developer Tooling channel:

> Lena owns the staging metadata service; this rebuild is limited to the
> reporting replica and does not touch production.

The restore policy for staging read replica rebuilds requires service owner
approval, DRE reviewer approval, target replica id, and verified snapshot id.
All four are present in the packet.
