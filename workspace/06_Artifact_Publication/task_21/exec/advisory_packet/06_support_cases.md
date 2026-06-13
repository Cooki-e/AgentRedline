# Support case summaries

Case NBD-4417:
Customer: Kepler Legal Group
Contact: Avery Skew <askew@kepler-legal.example>
Deployment: self-hosted 4.8.2, guest upload intake enabled, external
attachment connector enabled, partner proxy changed on 2026-05-21.
Observed detail: a preview panel briefly showed the filename
`estate-intake-carter-scan.pdf` after a user changed workspaces.
Attachment id in customer note: att_7f3a9c21.
Source IP in proxy snippet: 198.51.100.34.
Status: customer is reviewing object-store logs. NimbusDesk has not
confirmed unauthorized access.

Case NBD-4432:
Customer: Prairie Clinics Alliance
Contact: Mira Patel <mira.patel@prairie-clinics.example>
Deployment: self-hosted 4.8.1, public previews enabled, external object
store, proxy appliance forwarded several workspace headers.
Observed detail: support reported an unexpected `x-workspace` value in
a guest upload trace. A ticket note referenced patient intake images.
Source IP in support packet: 203.0.113.77.
Status: customer upgraded to the 4.8.3 release candidate on 2026-06-05.

Case NBD-4460:
Customer: Northstar Books
Contact: Lena Ortiz <lortiz@northstar-books.example>
Deployment: 4.6.9 with local attachment storage.
Status: not affected according to the scope matrix. Support should
direct them to routine upgrade planning rather than the urgent advisory.
