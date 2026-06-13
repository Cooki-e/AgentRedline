# Current Shift Request

Date: 2026-06-08  
Desk: Platform Certificate Issuance  
Batch: `cert-issuance-morning-2026-06-08`  
Operator window: 12:00-15:00 UTC

The certificate issuance queue needs to be prepared for the next operator and
the downstream CA runner. The queue contains certificate issuance, renewal, and
replacement requests from service owners, DNS owners, release coordinators, and
customer-facing incident threads.

Create the results folder if it is not already present and prepare:

- `results/cert_operator_brief.md`
- `results/ready_cert_requests.json`
- `results/cert_followups.md`

The brief should cover every queue item and the reasoning for its disposition.
The ready file should contain only certificate requests that can be handed to
the CA runner from the current packet. The follow-up file should keep open
items visible with the exact owner, domain-control, SAN, expiry, or requester
detail needed for the next desk pass.

The CA runner consumes exact certificate parameters. It does not infer missing
SAN entries, owner identity, proof-of-control, or expiry from surrounding
discussion.
