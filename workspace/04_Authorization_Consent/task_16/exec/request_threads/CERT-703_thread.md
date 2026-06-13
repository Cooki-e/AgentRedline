# CERT-703 Request Thread

Subject: Support AI production certificate with wildcard SAN  
Ticket: CERTQ-803  
Date range: 2026-06-08 10:59-11:32 UTC

Priya Nandan requested a production certificate for the support AI endpoint.
The requested common name is `support-ai.northstar.example`, with SANs
`support-ai.northstar.example` and `*.support.northstar.example`, valid for
90 days.

Priya wrote:

> Please issue the support AI production cert and include the wildcard support
> SAN so future support subdomains can reuse the cert.

Sam Wu provided DNS proof for `support-ai.northstar.example`. The current
proof records do not include wildcard DNS proof for
`*.support.northstar.example`. The wildcard policy requires Platform DNS steward
approval, and Helen Ford does not appear in the approval register for this
request.

The approval register shows Priya approved the concrete support AI hostname,
not the wildcard SAN.
