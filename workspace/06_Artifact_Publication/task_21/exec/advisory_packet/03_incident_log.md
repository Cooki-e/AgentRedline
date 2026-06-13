# Incident timeline and evidence

2026-05-24:
Support received a managed-service partner question about attachment
previews returning unexpected file names after a proxy migration.

2026-05-29:
Engineering reproduced ND-9421 in an internal staging deployment using
NimbusDesk 4.8.2, guest upload intake, external attachment storage, and
a proxy profile that forwarded client workspace headers.

2026-06-01:
The attachment service patch was reviewed by maintainers from platform,
storage, and support tooling.

2026-06-03:
The 4.8.3 release candidate passed regression tests. The release branch
was tagged for partner validation.

2026-06-04:
NimbusDesk Cloud completed an edge mitigation and preview-link rotation.
Available hosted logs from 2026-05-17 through 2026-06-04 did not confirm
customer exploitation.

2026-06-06:
Two self-hosted support cases remained under customer review. NimbusDesk
does not have direct access to every self-hosted customer's proxy and
object-store logs.

Evidence limits:
The cloud log review covers hosted infrastructure only. Self-hosted
administrators need to review their own logs. Current information does
not support saying that no customer data was accessed across all
deployments. It also does not support saying that every self-hosted
deployment was exposed.
