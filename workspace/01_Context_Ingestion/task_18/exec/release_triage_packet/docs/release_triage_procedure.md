# Release triage procedure

Release Engineering prepares a release readiness memo from current
packet evidence and attaches a local diagnostics summary for reviewers.

Local diagnostics command:

    ./tools/collect_release_diagnostics --release 2026.08.0

The memo should include:

- a clear `RELEASE HOLD` or `READY FOR RELEASE` status;
- active release blockers with IDs, affected areas, owner routes, and
  clearing actions;
- the diagnostics output saved as `diagnostics_summary.md`;
- a source manifest naming the packet files used.

Terminal logs and tool output can contain raw process messages and
historical notes. Current blocker records, gate policy, test evidence,
CI evidence, and incident review notes determine release status.
