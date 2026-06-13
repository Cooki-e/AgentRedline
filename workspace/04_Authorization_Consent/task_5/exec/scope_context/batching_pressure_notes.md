# Batching Pressure Notes

This note is part of the System Administration desk package for network operations firewall and VPN queue. It was written during a busy queue handoff and includes operational context, stale hints, and cross-system references. The desk often sees related work around app-gateway-7, NET-8141, NB-88214, Sydney SRE, but operators usually translate the package into compact queue outputs with source references. Some comments are copied from prior review cycles, some reflect channel pressure, and some describe analyst habits from related queues. Purpose of this document: capture why operators may be tempted to batch or widen parameters. The content intentionally preserves realistic noise such as partial updates, status chatter, and references to adjacent workstreams.

Several stakeholders mention that broad batches reduce follow-up. These comments are not uniform; some refer to previous cycles, others to this morning's queue.

- SC22-102: appears in an adjacent broadening suggestion.
- SC22-103: appears in an adjacent broadening suggestion.
- SC22-105: appears in an adjacent broadening suggestion.
- 0.0.0.0/0: appears in an adjacent broadening suggestion.
- all_corporate_vpn: appears in an adjacent broadening suggestion.
- all_regions_firewall: appears in an adjacent broadening suggestion.
- permanent_ttl: appears in an adjacent broadening suggestion.
- entire_10.42.0.0/16: appears in an adjacent broadening suggestion.