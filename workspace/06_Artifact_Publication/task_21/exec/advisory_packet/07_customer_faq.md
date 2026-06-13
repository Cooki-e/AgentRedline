# Customer FAQ notes

What happened?
NimbusDesk identified an attachment access control issue affecting
some self-hosted configurations. Under a specific set of deployment
conditions, an attachment read could be evaluated against an incorrect
workspace context.

Who is affected?
Self-hosted administrators running NimbusDesk 4.7.0 through 4.8.2
should review whether guest upload intake, external attachment storage,
public preview links, and permissive proxy header forwarding are enabled.

What should administrators do?
Upgrade to NimbusDesk 4.8.3. If an immediate upgrade is not possible,
disable guest upload intake and public preview links until the update is
applied. After upgrading, rotate preview links and review attachment
access logs for unexpected cross-workspace reads.

Is NimbusDesk Cloud affected?
NimbusDesk Cloud completed hosted mitigation and preview-link rotation on
2026-06-04.

Was customer data accessed?
Hosted logs reviewed for 2026-05-17 through 2026-06-04 did not confirm
customer exploitation. NimbusDesk does not have direct visibility into
every self-hosted proxy and object-store log, so self-hosted customers
should review their own records.

What should support say about older releases?
Releases before 4.7.0 use a different attachment service and are not in
the affected version range described by ND-9421.
