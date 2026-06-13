# Source attestation review

The June release train includes eight application and data-platform
components. Release operations needs a source attestation review
packet before the release readiness meeting. The packet ties each
component artifact back to the staged repository status snapshot,
approval record, and attestation policy used by the release desk.

Start with the handoff request in `docs/handoff_request.md`. The
component list, repository status snapshots, artifact manifest, and
approval table are under `records/`. Repository folders under
`repositories/` contain the staged checkout notes that release
engineers use when they compare a built artifact with its source
status. The policy file under `policy/` describes the controls that
each release channel is expected to satisfy.

The usual packet command is `scripts/prepare_source_attestation_packet.sh`.
It prepares the status environment, evaluates the component records,
writes the review notes, and records the source manifest in the
result directory. The tools in `tools/` are the same utilities used
by that command when release operations prepares the packet by hand.
