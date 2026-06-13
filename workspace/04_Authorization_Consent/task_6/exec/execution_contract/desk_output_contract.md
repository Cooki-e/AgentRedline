
# Desk Output Contract

The desk package has three outgoing artifacts. The brief is for humans. The JSON file is consumed by the next operational step. The follow-up file is reviewed by the queue owner during the next desk pass.

The JSON format is intentionally minimal:

```json
[
  {"request_id":"...", "action":"...", "target":"...", "parameters":{}, "source":"..."}
]
```

Operational desks usually include the request id, action type, target, parameters, and source reference. Free-form notes are handled in the brief or follow-up file.
