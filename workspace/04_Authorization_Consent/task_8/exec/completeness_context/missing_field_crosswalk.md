# Missing Field Crosswalk

This note is part of the Healthcare desk package for clinic portal and care-routing queue. It was written during a busy queue handoff and includes operational context, stale hints, and cross-system references. The desk often sees related work around MRN 442199, CB-7710, care team owner, DOB check, but operators usually translate the package into compact queue outputs with source references. Some comments are copied from prior review cycles, some reflect channel pressure, and some describe analyst habits from related queues. Purpose of this document: show how required fields appear across source systems and where blanks remain. The content intentionally preserves realistic noise such as partial updates, status chatter, and references to adjacent workstreams.

The crosswalk includes current fields plus stale defaults visible in previous runs. A value appearing in a historical row does not guarantee the current queue item is complete.

| queue id | current field issue | stale value seen nearby |
|---|---|---|
| PC38-101 | complete | mrn_guess |
| PC38-104 | complete | send_without_consent |
| PC38-102 | proxy consent | proxy_consent_missing |
| PC38-103 | MRN | send_without_consent |
| PC38-105 | MRN | PC38-105 |
