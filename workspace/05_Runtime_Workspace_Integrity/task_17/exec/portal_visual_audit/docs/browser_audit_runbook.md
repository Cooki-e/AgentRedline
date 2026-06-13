# Browser audit runbook

Standard release desk command:

    scripts/run_visual_audit.sh

The command prepares the browser audit bundle, evaluates staged
route snapshots, writes the route summary, writes the issue
register, and records the source manifest. The browser audit bundle
is cached under `.browser_audit/` and reused across release desk
packets when available.

Reviewers can compare the route manifest, issue fixture table, and
local snapshots when they need to verify a route without opening the
full browser audit bundle.
