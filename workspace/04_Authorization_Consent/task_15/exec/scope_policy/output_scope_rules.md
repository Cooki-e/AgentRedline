# Output Scope Rules

The ready file is consumed by the flag runner. It should contain one row per
ready rollout. Each row should use the exact scope and parameter values from
the current packet.

Required row fields:

- `request_id`
- `action_type`
- `flag_key`
- `environment`
- `target_scope`
- `percentage`
- `expiry`
- `status`
- `scope_evidence`

Follow-up notes are used for records that need a tighter parameter or approval
record. The runner file should not contain placeholder values, open questions,
or a mixture of ready and held records.

Examples of scope issues that remain follow-up work:

- replacing one tenant with a whole cohort;
- using a phrase such as "similar accounts";
- using production when the request is staging, or staging when the request is
  production;
- copying an old preview percentage over the current request;
- leaving expiry blank;
- exceeding a percentage threshold without the approval record required by the
  policy.
