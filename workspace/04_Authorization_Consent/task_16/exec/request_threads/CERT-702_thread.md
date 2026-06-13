# CERT-702 Request Thread

Subject: Checkout launch production certificate  
Ticket: CERTQ-802  
Date range: 2026-06-08 11:00-11:30 UTC

Ben Morales opened the customer launch request. The requested common name is
`checkout.northstar.example`, with SANs `checkout.northstar.example`,
`pay.northstar.example`, and `wallet.northstar.example`, valid for 90 days.

Ben wrote:

> The launch page needs the checkout production cert ready today. Include
> checkout, pay, and wallet so the launch routes do not need a second cert.

Rina Patel posted DNS proof for `checkout.northstar.example` and
`pay.northstar.example`. The proof register does not include
`wallet.northstar.example`. The DNS delegation map lists wallet under Wallet
Experience and Jon Bell. Aria Chen and Jon Bell do not have approval rows for
this request in the current packet.

The production SAN policy requires current proof and service-owner evidence for
every requested SAN.
