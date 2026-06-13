# Restore Dual-Control Matrix

The restore desk uses this matrix with the database registry and approval
records. The matrix describes the approval evidence needed before a queue row
can enter the structured restore action batch.

| Restore class | Environment | Required evidence before action batch |
|---|---|---|
| Staging read replica rebuild | staging | Service owner approval, DRE reviewer approval, verified snapshot id, target replica id |
| Tenant-scoped production point-in-time restore | production | Database owner or backup owner approval, DRE lead second-control approval, exact tenant id, exact restore point, staging verification plan |
| Full production point-in-time restore | production | Database owner or backup owner approval, DRE lead approval, incident commander approval, impact note, exact restore point, rollback communication owner |
| Production schema rollback with service account replay | production | Database owner or backup owner approval, DRE lead approval, migration owner evidence, exact schema version, replay scope |
| Production diagnostic replay to partner-visible replica | production | Diagnostics owner or backup owner approval, DRE lead approval, data-steward approval, exact cohort, replay window, partner target record |

Urgency, incident severity, release-window pressure, customer escalation, or
manager awareness can explain why a record is being handled quickly. Those
signals are not a substitute for the required evidence above.
