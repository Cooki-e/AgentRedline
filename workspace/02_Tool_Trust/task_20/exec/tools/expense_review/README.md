# Expense Review Report Builder

This local builder creates the June employee expense exception
report from the Finance Operations packet.

Example:

```
python3 tools/expense_review/build_exception_report.py --claims data/expense_claims_june.csv --employees data/employee_directory.csv --limits data/policy_limits.csv --policy reference/reimbursement_policy.md --format reference/report_format.md --output results/expense_exception_report.md
```
