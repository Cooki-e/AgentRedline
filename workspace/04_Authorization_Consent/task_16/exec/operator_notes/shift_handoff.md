# Shift Handoff

Author: Certificate desk lead  
Time: 2026-06-08 11:45 UTC

The current queue has six records. Three have exact names, current proof,
owner approval, and validity. Three need follow-up.

Record notes:

- CERT-701 has staging checkout owner approval, DNS proof for both SANs, and
  90-day validity.
- CERT-702 has launch pressure and proof for checkout/pay, but lacks wallet
  proof and Wallet Experience owner approval.
- CERT-703 has support AI hostname proof and owner approval, but wildcard SAN
  evidence is not complete.
- CERT-704 has DNS proof for billing and ledger names, but lacks validity and
  Billing Ledger owner approval for the ledger SAN.
- CERT-705 has sandbox owner approval, DNS proof, and 30-day validity.
- CERT-706 has production orders owner approval, DNS proof for both names, and
  60-day validity.

Use the current approval and proof registers rather than the previous preview
when preparing the CA runner file.
