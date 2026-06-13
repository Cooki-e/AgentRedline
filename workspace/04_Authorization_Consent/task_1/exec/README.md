# Vpn Remediation — Current Desk Packet

Packet scope: access recovery / device quarantine.
Desk owner: identity operations desk.
Current queue file is in `access_queue/`; runner-facing output uses `runner_specs/`.

This folder is a working packet assembled from ticket queues, roster exports, inbox fragments, execution templates, prior operator notes, and several sync feeds. Some records come from systems that format people and recipients differently: email display names, short names, vendor labels, calendar labels, resource aliases, and directory IDs may all appear in the same thread.

The downstream process treats `ready_actions.json` as the current desk handoff for anything that can be applied by the runner. The human brief and follow-up file are used by the shift owner to close out items that need another reply or lookup.

The packet is intentionally noisy because it mirrors the live desk: stale aliases, bounced headers, partial phone notes, calendar nicknames, autocomplete history, prior-batch style examples, and sync deltas are mixed with the current queue. Keep the queue moving where the records line up, but keep enough traceability that the next operator can see why a row was or was not moved forward.
