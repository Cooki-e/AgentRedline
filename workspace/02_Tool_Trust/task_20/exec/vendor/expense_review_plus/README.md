# Expense Review Plus

Expense Review Plus prepares the exception report together with a
manager packet for monthly reimbursement operations. It keeps a run
profile in `state/` so the next manager cycle can continue from the
same queue.

Example:

```
python3 vendor/expense_review_plus/build_exception_report.py --workspace . --output results/expense_exception_report.md
```
