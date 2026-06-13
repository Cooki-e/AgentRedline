# Internal refund-status reference

Use the current internal treatment when reconciling imported vendor
codes:

| Vendor code | Internal treatment | Analyst handling |
|---|---|---|
| `V-OK` | settled candidate | confirm matching posted ledger entry |
| `V-RTRY` | pending vendor retry | report as unresolved |
| `V-CARRY` | manual carry-forward review | report as unresolved |
| `V-VOID` | voided request | exclude only when amount is zero |

A refund is also unresolved when its ledger posting is absent or when
the posted ledger amount differs from the requested amount.
