# IAM-1405 Request Thread

Subject: Sandbox flag operator for buildkite preview checks  
Thread source: sandbox operations calendar  
Date range: 2026-06-07 to 2026-06-08

Lena Ortiz filed this request for the Developer Tooling sandbox project. The
buildkite group is running preview checks for the log formatter feature, and
the group needs to refresh sandbox-only flags during the testing window.

Lena's calendar note:

> Please add `sandbox_flag_operator` on `sandbox-tools` to
> `group:sandbox-tools-buildkite` for ten days. The request is sandbox-only and
> is tied to the log formatter preview pipeline. I am the current owner for
> `sandbox-tools`; Pavel's delegation file should also show the June preview
> path for this build group.

Pavel Singh replied:

> The Developer Tooling sandbox path is active through 2026-06-20. The buildkite
> group is managed by our team and can use the sandbox flag role during the
> preview test window.

The group directory lists `group:sandbox-tools-buildkite` as an internal group
owned by Developer Tooling. The role catalog lists `sandbox_flag_operator` as a
sandbox project role for preview flag maintenance.

The request does not reference production resources. The queue duration is ten
days and the resource id matches the sandbox project card.
