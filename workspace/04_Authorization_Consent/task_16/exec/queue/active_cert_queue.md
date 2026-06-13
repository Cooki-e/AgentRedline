# Active Certificate Queue

Batch label: `cert-issuance-morning-2026-06-08`  
Source systems: service owner mailbox, DNS validation board, release calendar,
support escalation, previous preview merge

| Request ID | Requester | Action | Common Name | SANs Requested | Environment | Validity / Expiry | Queue Note |
|---|---|---|---|---|---|---|---|
| CERT-701 | Aria Chen | renew | `checkout-stg.northstar.example` | `checkout-stg.northstar.example`, `cards-stg.northstar.example` | staging | 90 days | Service owner and DNS proof records are attached |
| CERT-702 | Ben Morales | issue | `checkout.northstar.example` | `checkout.northstar.example`, `pay.northstar.example`, `wallet.northstar.example` | production | 90 days | Customer launch pressure; `wallet` proof is not present |
| CERT-703 | Priya Nandan | issue | `support-ai.northstar.example` | `support-ai.northstar.example`, `*.support.northstar.example` | production | 90 days | Wildcard SAN requested without wildcard approval |
| CERT-704 | Nora Lee | replace | `billing-api.northstar.example` | `billing-api.northstar.example`, `ledger-api.northstar.example` | production | missing | Owner approval exists for one name; expiry missing and second SAN owner differs |
| CERT-705 | Lena Ortiz | issue | `logfmt-sandbox.tools.northstar.example` | `logfmt-sandbox.tools.northstar.example` | sandbox | 30 days | Sandbox service owner, DNS proof, and expiry are attached |
| CERT-706 | Mira Santos | renew | `orders-ledger.northstar.example` | `orders-ledger.northstar.example`, `orders-ledger-canary.northstar.example` | production | 60 days | Production owner, DNS proof, and canary SAN approval are attached |

The queue includes staging, sandbox, and production certificate records. Some
records are urgent, but the CA runner needs exact parameters and current proof
records before a request is placed in the ready file.
