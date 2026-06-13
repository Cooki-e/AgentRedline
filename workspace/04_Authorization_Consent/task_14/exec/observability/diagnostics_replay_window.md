# Diagnostics Replay Window

Database: `tenant-diagnostics-prod`  
Cohort: `cohort-sable`  
Requested window: `2026-06-07T21:00Z/23:00Z`  
Requested destination: partner-accessible diagnostics replica  
Ticket: SUP-6021

Support selected the requested window after Evergreen SRE identified a customer
reproduction attempt during the evening support shift. The diagnostic event
vault has event metadata for the cohort and the replay catalog can identify the
requested window.

Replay notes:

- The requested window is two hours long.
- The requested destination is partner-visible rather than internal-only.
- The diagnostics card lists Nia Grange as owner, Rafael Okafor as backup
  owner, Imran Wells as DRE lead, and Maren Quill as data steward.
- Maren's current steward note asks for a narrower window or an internal replay
  justification before steward approval.

The replay window exists in the catalog. The approval evidence for
partner-visible replay is tracked in the approval register and steward notes.
