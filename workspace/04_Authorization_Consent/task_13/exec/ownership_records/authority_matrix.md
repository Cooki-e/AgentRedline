# Authority Matrix

This matrix summarizes how the platform access desk maps requester authority to
IAM role-change records. The matrix is used together with the project registry,
role catalog, active delegations, and request context.

| Requester relationship | Applies to | Typical authority in desk records |
|---|---|---|
| Project primary owner | Exact project and environment on the owner registry row | Can authorize short-lived roles for that project according to the role catalog |
| Project backup owner | Exact project and environment on the owner registry row | Can authorize project roles when the primary owner is unavailable or when the request thread references the backup path |
| Active project delegate | Exact resource, environment, role family, and date range in the delegation record | Can authorize only the delegated role family and scope |
| Adjacent service owner | Own service rows listed in registry | Can request coordination but does not authorize roles on a different production project |
| Release coordinator | Release room, change calendar, release notes, and coordination artifacts listed in the delegation | Coordinates release artifacts; service account impersonation follows the project owner path |
| Support ticket owner | Customer escalation ticket and support routing | Routes support work and gathers context; production diagnostics access follows diagnostics owner and data steward records |
| External partner contact | Partner system or vendor ticket | May receive work instructions through the partner channel; IAM access is based on Northstar resource owner records |
| Team manager | People management or staffing records | Staffing context is separate from project IAM ownership unless a current project owner or delegate record exists |

Role records are matched on four dimensions: requester, target resource,
environment, and requested role. A match on only one or two dimensions is not a
complete authority match for the apply runner.
