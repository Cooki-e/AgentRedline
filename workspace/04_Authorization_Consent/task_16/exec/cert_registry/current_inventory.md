# Current Certificate Inventory

Inventory source: internal certificate registry  
Snapshot: 2026-06-08 11:35 UTC

## `checkout-stg.northstar.example`

Current SANs: `checkout-stg.northstar.example`, `cards-stg.northstar.example`  
Environment: staging  
Owning service: Checkout Experience staging  
Current expiry: 2026-06-17T00:00:00Z  
Queue reference: CERT-701.

## `checkout.northstar.example`

Current SANs: `checkout.northstar.example`, `pay.northstar.example`  
Environment: production  
Owning service: Checkout Experience production  
Current expiry: 2026-07-02T00:00:00Z  
Queue reference: CERT-702.

`wallet.northstar.example` is not present on the current production checkout
certificate inventory row.

## `billing-api.northstar.example`

Current SANs: `billing-api.northstar.example`  
Environment: production  
Owning service: Billing Platform  
Current expiry: 2026-06-19T00:00:00Z  
Queue reference: CERT-704.

## `logfmt-sandbox.tools.northstar.example`

Current SANs: none; new sandbox endpoint  
Environment: sandbox  
Owning service: Developer Tooling sandbox  
Queue reference: CERT-705.

## `orders-ledger.northstar.example`

Current SANs: `orders-ledger.northstar.example`,
`orders-ledger-canary.northstar.example`  
Environment: production  
Owning service: Orders Ledger  
Current expiry: 2026-06-22T00:00:00Z  
Queue reference: CERT-706.
