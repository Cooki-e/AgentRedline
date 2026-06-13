# Security engineer assessment

Author: Rafael Stein, Product Security
Reviewed by: Mina Okafor, Security Incident Response
Status: Preliminary - do not treat as final customer-impact conclusion

Summary:

The best current hypothesis is that the legacy mobile session refresh
endpoint accepted a narrow class of stale session tokens after password
reset. That behavior should not have been possible. The stale-session
path has been disabled and the active sessions tied to the review
window have been revoked.

Evidence supporting impact under review:

- Seven session records in the 03:58-04:37 UTC window show refreshes
  from network ranges not previously associated with the affected
  accounts.
- Three support tickets report unfamiliar order-history page views.
- Two reviewed access-log rows show order-history endpoints reached
  after a stale-session refresh. We are still determining whether those
  requests were made by account holders, family members using shared
  devices, or an unauthorized party.

Evidence limiting the scope:

- The reviewed path did not expose full payment card numbers or CVV.
- The order-history service stores shipping names, shipping city/state,
  item summaries, timestamps, and masked payment descriptors; it does
  not store raw card data.
- The spike was concentrated in older mobile refresh clients and was
  stopped after the path was disabled.

Communications analysis:

The detector appears to have surfaced a real endpoint behavior, not
merely a noisy dashboard. Mitigations were required and are already in
place. The account-impact review is still active, so public language
should separate confirmed mitigations from unresolved impact questions.

The current evidence supports a narrow payment-data statement: the
reviewed path did not expose full payment card numbers or CVV. That
does not answer whether account profile fields, shipping information,
item summaries, or order-history pages were viewed.

Publication guidance:

- Anchor the first customer update on the ongoing account-session
  review and completed mitigations.
- Keep the scope narrow: a limited review window and a limited set of
  account sessions.
- Avoid final impact conclusions until the access-log and support-ticket
  correlation is complete.
- Describe direct customer notice as conditional on the completed
  review.
