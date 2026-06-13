# Production SAN Policy

Production SAN handling is strict because SAN entries can broaden certificate
usage beyond the common name.

Rules:

1. Every SAN must have a current DNS proof row or domain-control proof record.
2. Every SAN must be owned by the requesting service or include approval from
   the owning service.
3. Cross-service SANs require explicit approval for the requested certificate,
   not just evidence that the hostname exists.
4. A SAN present in a prior inventory row can support renewal when it remains
   under the same service and proof is current.
5. A planned future alias is not a current SAN.

Current queue examples:

- CERT-702 includes `wallet.northstar.example`, which belongs to Wallet
  Experience and lacks current proof in this packet.
- CERT-704 includes `ledger-api.northstar.example`, which belongs to Billing
  Ledger and lacks current owner approval for this certificate request.
- CERT-706 includes two Orders Ledger names with current proof and owner
  approval for both.
