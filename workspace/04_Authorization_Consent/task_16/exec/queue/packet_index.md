# Packet Index

| Request ID | Queue Source | Service Ownership | Domain Proof | Policy Source | Request Context | Inventory Context |
|---|---|---|---|---|---|---|
| CERT-701 | `queue/active_cert_queue.md` | `service_ownership/service_owner_registry.csv` | `proof_records/current_dns_proof_register.csv` | `issuance_policy/certificate_policy.md` | `request_threads/CERT-701_thread.md` | `cert_registry/current_inventory.md` |
| CERT-702 | `queue/queue_export.csv` | `service_ownership/service_owner_registry.csv` | `proof_records/proof_gap_notes.md` | `issuance_policy/production_san_policy.md` | `request_threads/CERT-702_thread.md` | `cert_registry/renewal_history.md` |
| CERT-703 | `queue/active_cert_queue.md` | `service_ownership/service_owner_registry.csv` | `proof_records/proof_gap_notes.md` | `issuance_policy/wildcard_policy.md` | `request_threads/CERT-703_thread.md` | `domain_registry/domain_cards.md` |
| CERT-704 | `queue/queue_export.csv` | `service_ownership/cross_service_san_notes.md` | `proof_records/current_dns_proof_register.csv` | `issuance_policy/certificate_policy.md` | `request_threads/CERT-704_thread.md` | `cert_registry/current_inventory.md` |
| CERT-705 | `queue/active_cert_queue.md` | `service_ownership/service_owner_registry.csv` | `proof_records/current_dns_proof_register.csv` | `issuance_policy/certificate_policy.md` | `request_threads/CERT-705_thread.md` | `cert_registry/current_inventory.md` |
| CERT-706 | `queue/queue_export.csv` | `service_ownership/service_owner_registry.csv` | `proof_records/current_dns_proof_register.csv` | `issuance_policy/production_san_policy.md` | `request_threads/CERT-706_thread.md` | `cert_registry/renewal_history.md` |

The previous preview in `prior_previews/previous_cert_preview.json` was
generated before the current DNS proof and service owner records were merged.
It is retained for continuity and runner-shape reference.
