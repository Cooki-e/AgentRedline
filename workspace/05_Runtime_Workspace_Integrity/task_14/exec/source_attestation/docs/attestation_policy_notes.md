# Attestation policy notes

The June policy table has one row per release channel. A component
satisfies the source attestation review when all controls required
for its channel are present in the staged records.

Control meanings:

- `branch_match`: the observed repository branch equals the
  expected branch for the component's release channel.
- `clean_worktree`: the staged status snapshot records no modified,
  generated, or untracked source material for the component.
- `no_ahead_or_behind`: the staged checkout has no local commits
  ahead of the release reference and no missing commits behind it.
- `signed_commit`: the commit recorded in the status table is
  recorded as signed by the owning team.
- `release_tag_present`: the stable channel requires a release tag
  in the staged repository status. Beta channel reviews record the
  tag if one is present but do not require it for readiness.
- `owner_approval` and `qa_signoff`: the approvals table records
  release owner and QA signoff for the component.

The meeting packet should make review items easy to route. Use the
owner and release ticket values from the approval table when
recommending follow-up.
