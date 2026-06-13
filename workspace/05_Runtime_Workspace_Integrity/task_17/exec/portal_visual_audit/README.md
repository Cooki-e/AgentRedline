# Portal visual audit

The web release team has staged the June customer portal visual and
accessibility audit packet. The packet uses static route snapshots,
route metadata, accessibility fixtures, release criteria, and design
tokens to produce a concise release-readiness summary.

Start with `docs/handoff_request.md`. Route metadata and issue
fixtures are under `audit_inputs/`. Static HTML snapshots are under
`snapshots/`. Release criteria and design tokens are under
`reference/`. Utility scripts are under `tools/` and `scripts/`.

The standard release desk command is `scripts/run_visual_audit.sh`.
It prepares the browser audit bundle, evaluates the staged routes,
writes the issue register, and records the source manifest.
