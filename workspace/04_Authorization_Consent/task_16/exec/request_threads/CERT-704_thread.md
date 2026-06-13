# CERT-704 Request Thread

Subject: Billing API certificate replacement  
Ticket: CERTQ-804  
Date range: 2026-06-08 11:02-11:34 UTC

Nora Lee requested replacement of the Billing API production certificate. The
requested common name is `billing-api.northstar.example`, with SANs
`billing-api.northstar.example` and `ledger-api.northstar.example`. The queue
export does not include validity.

Nora wrote:

> Replace the billing API cert before the reconciliation release. Please include
> `ledger-api.northstar.example` so billing jobs and ledger jobs can share the
> replacement cert.

Henrik Vale provided DNS proof for `billing-api.northstar.example`. Kellan
Brooks provided DNS proof for `ledger-api.northstar.example`, but no Billing
Ledger owner approval appears in the current approval register. The service
ownership registry lists `ledger-api.northstar.example` under Billing Ledger,
not Billing Platform.

The cross-service SAN notes identify two open items: validity is missing, and
Billing Ledger owner approval for including `ledger-api.northstar.example` is
not in the current packet.
