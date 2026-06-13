# Runner Error Examples From Past Batches

These examples are included for operator training and formatting context. They are intentionally brief.

- A row with a valid JSON shape but stale mailbox was accepted by the runner and routed to a shared inbox. The brief mentioned the ambiguity, but the action file did not carry the hold state.
- A queue row with two possible recipients was written as `status: ready` because the latest reply used a first name. The runner could not tell the difference between the two principals.
- A safe service-principal update was delayed because an adjacent customer-recipient row was messy; the reviewer marked that as unnecessary blocking.

The desk now tries to keep the action file small and the human brief explanatory.
