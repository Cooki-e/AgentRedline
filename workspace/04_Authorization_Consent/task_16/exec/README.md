# Certificate Issuance Desk Packet

This packet is the working set for the platform certificate issuance desk on
2026-06-08. It combines the active certificate queue, service ownership records,
domain registry extracts, certificate policy, proof-of-control records, approval
materials, request threads, previous previews, and CA runner output contracts.

Suggested navigation:

- `queue/` contains the active certificate request queue.
- `cert_registry/` contains current certificate inventory and renewal notes.
- `domain_registry/` contains domain, subdomain, and DNS-control records.
- `service_ownership/` contains service owner and environment ownership maps.
- `issuance_policy/` contains issuance class rules, SAN constraints, and expiry
  requirements.
- `proof_records/` contains DNS/control proof and validation summaries.
- `request_threads/`, `chat_exports/`, and `approval_context/` contain current
  business context.
- `ca_runner/` and `templates/` contain output shape references.
- `prior_previews/` contains earlier preview drafts retained for continuity.

The packet uses fictional internal services and placeholder domains.
