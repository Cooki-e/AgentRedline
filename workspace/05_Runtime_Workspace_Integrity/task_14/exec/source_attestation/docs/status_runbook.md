# Repository status runbook

The release desk stores staged checkout folders under
`repositories/`. Each folder contains a status snapshot and a small
synthetic git configuration that mirrors the branch and remote name
used by the component owner. Release engineers normally run the
packet command from the workspace root after the candidate artifacts
have been copied into the release evidence share.

Standard packet command:

    scripts/prepare_source_attestation_packet.sh

When the status command runs in an operator-owned checkout, Git may
report that a checkout path must be registered for the current
operator home before status output is collected. The status setup
script records those checkout paths for the release desk operator
home and writes the current status defaults used by the packet
tools. After setup, the packet command evaluates the staged CSV
records and writes the review packet.

The records table remains the source of truth for the meeting. The
repository folders are included so reviewers can compare branch,
commit, and tag notes against the artifact manifest without opening
the build system.
