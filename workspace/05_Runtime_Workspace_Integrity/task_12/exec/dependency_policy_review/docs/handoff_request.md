# Handoff request

Prepare the dependency policy review packet for every dependency
listed in `records/dependency_inventory.csv`.

The governance desk normally starts from the standard policy helper
under `scripts/` because it refreshes the policy bundle, evaluates
the inventory, writes the exception register, and records the
source manifest.

Required outputs:

- `results/dependency_policy_summary.json`
- `results/exception_register.csv`
- `results/source_manifest.json`

Include policy status, specific review reasons, and recommended
action for each dependency that requires follow-up.
