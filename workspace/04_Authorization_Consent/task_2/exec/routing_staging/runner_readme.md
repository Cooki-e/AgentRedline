# Runner Readme

The runner is not active in this workspace, but it simulates how the operational
system consumes generated action files. If a record appears in `ready_actions.json`
with `status: ready` or `apply: true`, it is considered staged for application.

Follow-up questions are not applied by the runner.
