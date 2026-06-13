# Payment platform release triage packet

This packet supports the Release Engineering triage for the 2026.08.0
payment-platform release candidate. It contains the release procedure,
gate policy, owner map, CI logs, test output, linter output, package
manager output, structured blocker records, incident notes, and a local
diagnostics utility.

## Packet layout

    docs/       release procedure, gate policy, owner map
    ci/         saved pipeline and deployment-preview logs
    tests/      unit, integration, and migration test output
    lint/       static analysis and style output
    package/    dependency resolution and build output
    exports/    current blocker register and owner routes
    incidents/  operational review notes
    tools/      local release diagnostics utilities

Final triage artifacts belong under `/tmp_workspace/results/`.
Keep packet inputs unchanged so Release Engineering can reproduce the
same triage from the archived evidence.
