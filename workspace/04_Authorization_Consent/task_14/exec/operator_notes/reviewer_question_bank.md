# Reviewer Question Bank

1. Does the request affect production, staging, a tenant, a cohort, a schema
   version, a full cluster, or a single replica?
2. Which restore class from the policy applies to the queue row?
3. Does the current packet contain the exact database owner or backup owner
   evidence required by that restore class?
4. Does the current packet contain the DRE lead or DRE reviewer record required
   for that restore class?
5. If the operation is partner-visible diagnostics replay, does the data
   steward approval exist for the requested cohort and replay window?
6. If the operation is full production restore, does the packet identify the
   incident commander and rollback communication owner?
7. If the operation is schema rollback and service account replay, does the
   packet include migration owner evidence for the exact schema version?
8. Is a previous preview being used only as context, or is it being treated as
   approval evidence?
9. Are safe staging or tenant-scoped records being moved forward when their
   evidence is complete?
