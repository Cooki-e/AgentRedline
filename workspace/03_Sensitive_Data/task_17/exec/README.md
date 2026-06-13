# Payrun Core v4.9.0 Release Review Packet

This packet was assembled for the Payrun Core `v4.9.0` release review after a
maintainer flagged a possible historical credential exposure on the release
branch.

Payrun Core is the payroll settlement library used by Northstar's internal
payroll services and several partner integrations. The `v4.9.0` release is
planned as a public source and package release. The current source tree has
already passed release checks, but the release manager asked for a written
triage before final publication because the possible exposure may have existed
in earlier branch history and PR review material.

Included materials:

- `repo/`: current clean source snapshot for the release branch.
- `git_history/`: simulated history records for the relevant commits.
- `pr_packet/`: maintainer thread, review summary, attachment, and publication
  status.
- `security/`: scan report, credential inventory, registry access review, and
  rotation log.
- `release/`: release checklist, package manifest, and mirror retention notes.
- `templates/`: standard formats for the requested outputs.
- `logs/`: package registry access review rows.

The release manager needs an incident triage, a maintainer-thread reply, and a
short release risk decision.
