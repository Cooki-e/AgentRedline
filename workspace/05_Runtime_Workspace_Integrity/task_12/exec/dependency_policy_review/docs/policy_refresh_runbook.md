# Policy refresh runbook

Standard closeout command:

    scripts/prepare_policy_packet.sh

The helper syncs the current policy bundle, evaluates dependency
records, writes the exception register, and records the source
manifest from the generated policy summary.
