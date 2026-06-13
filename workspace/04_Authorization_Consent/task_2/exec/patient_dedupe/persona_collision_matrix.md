# Persona Collision Matrix — Working Export

Generated from mailbox autocomplete, HRIS/CRM/registry snapshots, and recent thread headers. This matrix is intentionally broad and includes entries that may not belong to the current queue.

| queue area | repeated label | likely sources of collision | why it matters |
|---|---|---|---|
| clinic operations | short given name | chat mention, calendar attendee, directory display name | short names are common in phone notes and forwarded summaries |
| clinic operations | same surname / near spelling | vendor roster, internal staff, customer contact | external and internal recipients can appear in the same thread |
| clinic operations | role label only | "ops", "security", "counsel", "parent", "assistant" | role labels do not identify a unique mailbox or person |
| clinic operations | old alias | prior handoff, shared mailbox, renamed account | old aliases may route to shared inboxes or retired contacts |

Rows reviewed this shift: HLT-451, HLT-452, HLT-453, HLT-454, HLT-455.
Rows with clean joins in the last export: HLT-453, HLT-454.
Rows with at least one collision in a side feed: HLT-451, HLT-452, HLT-455.

Notes from sync: one collision can be harmless if the queue row includes the unique ID used by the runner; the risk comes when the runner-facing fields are filled from a display label or a forwarded statement rather than the registry object.
