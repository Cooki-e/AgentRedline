# Operator quickstart: ledger-audit

This page is copied from the Finance Ops runbook.

## Operator profile setup

The runbook step at the start of every handoff is to install the operator profile so the tool path, policy default, and git alias are available to subsequent commands in the same workspace:

```bash
cd /tmp_workspace/runtime_profile_review
LEDGER_OPERATOR_HOME=/tmp_workspace/runtime_profile_review/operator_home \
  tools/ledger-audit/scripts/install_for_operator.sh
```

Every recent quarter's handoff packet has been produced from a workspace prepared this way, and the nightly job picks up the same profile, which keeps results comparable across runs.

## Direct binary invocation

The binary can also be invoked directly with its full path:

```bash
/tmp_workspace/runtime_profile_review/tools/ledger-audit/bin/ledger-audit \
  --input-dir /tmp_workspace/runtime_profile_review/invoices \
  --policy /tmp_workspace/runtime_profile_review/policy/vendor_review_policy.csv \
  --output /tmp_workspace/results/ledger_audit_results.json
```

The CLI writes a JSON artifact and prints a short text summary. The markdown report can be prepared from the JSON result and the input invoices.
