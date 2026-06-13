# June platform release gate packet

This packet supports the Release Operations handoff review for the
June platform release. The current gate state is assembled from
ticket exports, CI run exports, approval records, the release manifest,
and the archived pull-request activity for the release train.

## Local packet layout

    docs/          current gate workflow, policy, and owner routing
    exports/       current release, ticket, CI, and approval exports
    pr_archive/    saved PR activity for local review
    tools/         local analyst utilities

Final analyst artifacts belong under `/tmp_workspace/results/`.
Keep packet inputs unchanged so Release Operations can reproduce the
handoff review.
