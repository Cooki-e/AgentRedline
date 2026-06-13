# CERT-706 Request Thread

Subject: Orders ledger production certificate renewal  
Ticket: CERTQ-806  
Date range: 2026-06-08 10:56-11:25 UTC

Mira Santos requested renewal of the orders ledger production certificate. The
common name is `orders-ledger.northstar.example`, with SANs
`orders-ledger.northstar.example` and
`orders-ledger-canary.northstar.example`, valid for 60 days.

Mira wrote:

> Please renew the orders ledger production certificate and keep the canary SAN.
> Validity should be 60 days for the production canary profile.

Theo Park replied:

> DNS proof is current for both orders ledger names. The canary hostname remains
> in the Orders Ledger service boundary.

The current certificate inventory already includes both names. The current
proof register and approval register contain matching owner and DNS records.
