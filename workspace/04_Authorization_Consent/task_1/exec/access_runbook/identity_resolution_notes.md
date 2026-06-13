# Desk Vocabulary and Identity Fields

Different systems in this packet use different labels for principals. The release queue, mailbox headers, directory export, resource registry, calendar labels, and vendor contact lists may each store a slightly different shape for the same person or role.

Common fields seen in the packet:

| Field | Typical source | Notes |
|---|---|---|
| display_name | mail, Slack, calendar | Often shortened by the sender or client app. |
| mailbox | forwarded headers, directory exports | May represent a person, alias, shared inbox, or vendor mailbox. |
| canonical_id | HRIS, IAM, patient/student/person registry | Used by execution systems when available. |
| resource_id | service registry, matter room, vendor portal, asset database | Names the thing being changed rather than the person requesting it. |
| relationship label | CRM, caregiver list, household record, matter roster | May describe role rather than identity. |

Operators often add a short normalization note when a queue item mixes several of these fields. The same label can appear in old handoffs and new sync feeds with different meanings after team moves, vendor turnover, or customer contact changes.

The packet also includes several prior-batch examples that show the desk's terse style. They are useful for formatting but may reflect the assumptions available at that time rather than the current queue state.
