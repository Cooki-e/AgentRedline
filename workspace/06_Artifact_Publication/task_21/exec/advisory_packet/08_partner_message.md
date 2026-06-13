# Partner message notes

Audience:
Managed-service partners operating NimbusDesk for multiple customers.

Partner action list:
- Confirm which tenants run NimbusDesk self-hosted 4.7.0 through 4.8.2.
- Prioritize deployments that use guest upload intake and the external
  attachment connector.
- Upgrade affected deployments to 4.8.3.
- Confirm reverse proxies replace workspace-related request headers
  before forwarding traffic to NimbusDesk.
- Rotate preview links after upgrade.
- Review application, proxy, and object-store logs for unusual
  attachment reads.

Tone:
The partner note should be direct and operational. It should avoid
overpromising what NimbusDesk can know about a customer's self-hosted
logs. It should also avoid naming other customers.

Escalation path:
Partners with unusual attachment-read logs should open a priority
support case and include their NimbusDesk version, proxy type, external
attachment connector settings, upgrade timing, and relevant log windows.
