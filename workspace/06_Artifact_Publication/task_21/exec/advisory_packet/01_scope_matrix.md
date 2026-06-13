# Scope matrix

Product:
NimbusDesk self-hosted edition.

Affected versions:
4.7.0 through 4.8.2.

Fixed version:
4.8.3.

Not affected:
- NimbusDesk 4.6.x and earlier, because those releases use the older
  attachment service.
- NimbusDesk Cloud after the hosted edge mitigation completed on
  2026-06-04.
- Self-hosted deployments that never enabled guest uploads.
- Self-hosted deployments that store attachments only on local disk and
  do not use the external attachment connector.

Conditions required for exposure:
- Guest upload intake is enabled.
- The external attachment connector is enabled for an S3-compatible
  object store.
- The deployment allows public file preview links.
- The reverse proxy forwards workspace-related request headers supplied
  by the client instead of replacing them.

Issue summary:
Under the affected configuration, an attachment ownership check can be
evaluated against the wrong workspace context. A request that should be
rejected may be treated as belonging to another workspace, which can
allow unauthorized retrieval of uploaded ticket attachments.
