# Validation Summary

Validation run: 2026-06-08 11:30 UTC  
Tooling source: certificate desk validation aggregator

| Request ID | Name Proof | Owner Evidence | Validity | SAN Scope | Summary |
|---|---|---|---|---|---|
| CERT-701 | complete | complete | 90 days | same-service staging SANs | Ready shape supported by current packet |
| CERT-702 | incomplete | incomplete for wallet alias | 90 days | includes future wallet alias | Needs wallet proof and owner path |
| CERT-703 | incomplete for wildcard | incomplete for wildcard | 90 days | wildcard SAN | Needs wildcard proof and platform DNS steward |
| CERT-704 | proof complete | incomplete for ledger SAN | missing | cross-service SAN | Needs validity and Billing Ledger owner approval |
| CERT-705 | complete | complete | 30 days | single sandbox name | Ready shape supported by current packet |
| CERT-706 | complete | complete | 60 days | same-service production/canary SANs | Ready shape supported by current packet |

The validation aggregator checks current packet evidence. It does not write CA
runner rows.
