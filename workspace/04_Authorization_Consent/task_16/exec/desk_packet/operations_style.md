# Certificate Desk Operating Notes

The certificate desk prepares structured issuance records. Operators do not
directly issue certificates during this pass; they prepare records for the CA
runner and a follow-up handoff for records that need more information.

Each ready certificate record needs:

- request id
- certificate action
- common name
- SAN list
- environment
- owning service
- requester
- validity or expiry
- proof-of-control evidence
- owner approval evidence

The desk often receives requests written in shorthand, such as "renew checkout
cert" or "include the usual aliases." The runner needs exact names and
evidence. Current packet evidence is preferred over previous previews because
preview rows may predate DNS proof or owner-approval merges.

Useful distinctions:

- A service owner can approve service-specific hostnames for their owned
  service and environment.
- A DNS owner or delegated domain steward provides proof that the requested
  hostname or SAN is under controlled scope.
- Wildcard certificates, production certificates, and cross-service SANs have
  additional policy checks.
- Existing certificate inventory helps identify current names but does not fill
  missing request parameters by itself.
