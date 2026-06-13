# Domain Cards

## `northstar.example`

Domain owner: Platform DNS  
Primary steward: Helen Ford, `helen.ford@northstar.example`  
Delegated service subdomains: checkout, billing, orders, support, tools  
Notes: Service-specific names under this domain are delegated to service owners
when the service ownership registry and DNS proof register agree.

## `checkout.northstar.example`

Service family: Checkout Experience  
DNS owner: Rina Patel  
Allowed hostnames in current proof register: `checkout.northstar.example`,
`pay.northstar.example`, `checkout-stg.northstar.example`,
`cards-stg.northstar.example`.  
Queue references: CERT-701 and CERT-702.

## `support.northstar.example`

Service family: Support Platform  
DNS owner: Sam Wu  
Allowed hostname in current proof register: `support-ai.northstar.example`.  
Wildcard delegation: not listed in current proof register.  
Queue reference: CERT-703.

## `billing.northstar.example`

Service family: Billing Platform and Billing Ledger  
DNS owners: Henrik Vale for Billing Platform, Kellan Brooks for Billing Ledger  
Allowed current proof names: `billing-api.northstar.example`,
`ledger-api.northstar.example`.  
Queue reference: CERT-704.

## `tools.northstar.example`

Service family: Developer Tooling  
DNS owner: Pavel Singh  
Allowed current proof names: `logfmt-sandbox.tools.northstar.example`.  
Queue reference: CERT-705.

## `orders.northstar.example`

Service family: Orders Ledger  
DNS owner: Theo Park  
Allowed current proof names: `orders-ledger.northstar.example`,
`orders-ledger-canary.northstar.example`.  
Queue reference: CERT-706.
