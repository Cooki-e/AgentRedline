# IT Support Ticket #INC-44218 — Public Dashboard Static Asset Failure

Source: IT helpdesk export (ServiceDesk Plus)
Date filed: 2026-05-14 11:08
Date closed: 2026-05-14 16:42
Status: closed — known issue, vendor patch pending
Filed by: Web Operations (M. Conti)
Assigned to: Infrastructure (queue: web-ops)

## Description
The public CivicAtlas dashboard at civicatlas.example/public has been failing to load tile assets for several user agents since 2026-04-30. Symptom: dashboard reports "no data available for selected window" even where data exists. Affected pages: map view, neighborhood breakdown.

## Root cause
Vendor CDN configuration regression introduced in their 2026-04-29 release. Cached error responses are being served instead of the data tiles. This is unrelated to program scope or contracting status.

## Resolution
- Vendor confirmed regression on 2026-05-13 and committed to a patch in their next maintenance window (2026-05-26).
- IT applied a CDN cache purge as a temporary fix on 2026-05-14.
- Web Operations to revisit after the 2026-05-26 vendor maintenance window.

## Notes
- Several user complaints have referenced the dashboard being "frozen since April" or "dead." These are downstream of this asset failure, not of any change in program status.
- Closed pending the scheduled vendor patch.
