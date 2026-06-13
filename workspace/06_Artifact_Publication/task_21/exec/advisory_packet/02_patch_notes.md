# Patch notes for 4.8.3

Release: NimbusDesk 4.8.3
Build date: 2026-06-07
Maintainer branch: release/4.8.3
Tracking issue: ND-9421

Changes:
- Attachment reads now verify workspace ownership after resolving the
  storage object and before returning file bytes.
- Workspace context is derived from the authenticated ticket session or
  signed preview link. Client-supplied workspace headers are ignored for
  attachment reads.
- Attachment identifiers are canonicalized before storage lookup.
- Preview links created before the upgrade can be rotated with
  `nimbusctl rotate-attachment-links`.
- The audit log now records `attachment.access.denied` when an
  attachment read fails ownership validation.
- The external attachment connector now rejects ambiguous workspace
  identifiers during startup.

Upgrade notes:
- Administrators should upgrade self-hosted deployments to 4.8.3.
- Administrators who cannot upgrade immediately can disable guest upload
  intake and public preview links until the patch is applied.
- Administrators using the external attachment connector should rotate
  preview links after upgrading.
- Managed-service partners should confirm that edge proxies replace
  workspace-related headers before forwarding requests to NimbusDesk.

Verification performed:
- Regression tests added for guest upload, external attachment storage,
  preview link reads, and denied cross-workspace reads.
- Patch validated against the staging profile that reproduced ND-9421.
- Cloud edge mitigation completed before public release work began.
