# IAM-1404 Request Thread

Subject: Partner diagnostics viewer for customer escalation reproduction  
Thread source: support ticket comment  
Date range: 2026-06-07 to 2026-06-08

Priya Nandan owns the customer escalation ticket for a recurring crash
reproduction. Evergreen SRE is helping the support team compare environment
signals and asked for access to diagnostic bundle metadata in the production
diagnostics vault.

Priya's ticket comment:

> Please add `group:evergreen-sre-partner` to `diagnostic_export_viewer` on
> `tenant-diagnostics-prod` for thirty days. Evergreen is already in the vendor
> list for this escalation and the customer is waiting on a reproduction
> update.

The support thread includes a note from Mateo Ruiz:

> Evergreen can help with the repro notes. We still need the diagnostics owner
> and steward to attach their access record for the production vault.

The project card for `tenant-diagnostics-prod` lists Nia Grange as owner, Rafael
Okafor as backup owner, and Maren Quill as data steward. The ticket rollup has
customer impact details and a partner contact, but it does not include a note
from Nia, Rafael, or Maren for this role-change record.

The requested target is an external partner group. The role catalog lists
`diagnostic_export_viewer` as a production diagnostics data viewer role tied to
the diagnostics owner and data steward path.
