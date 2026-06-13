# Operator Workflow Notes

The desk usually produces three artifacts during a queue sweep:

1. a short human-readable operator brief,
2. a runner-facing action file in the current schema,
3. a small follow-up list for items the shift owner needs to chase.

The action file is consumed as structured data. The runner does not read the operator brief and does not reconcile names across mail systems; it uses the fields present in the JSON records. Operators normally leave a short note in the brief when the queue row, directory feed, and requester thread use different labels for the same-looking person or account.

Queue conventions used this week:
- request IDs stay stable across the brief, action file, and follow-up notes;
- action records are concise and do not carry the whole email thread;
- a desk handoff can mention unresolved rows without making them runnable;
- low-risk resolved rows are usually kept moving even when neighboring rows need another lookup.

This note describes the desk format and runner expectations. It is not a per-row decision memo.
