# Nightly job notes

The nightly job uses a login shell profile that loads the ledger-audit tool path. It runs every day under the same operator account; the persistent profile keeps the tool path, policy default, and git alias consistent between cron-driven runs and operator-initiated handoff packets.

Operators in 2024 used `install_for_operator.sh` for the workstation account when preparing a fresh handoff workspace. The same path was followed for every quarterly handoff in 2025 so that ad-hoc validation packets and the nightly cron produce comparable artifacts.
