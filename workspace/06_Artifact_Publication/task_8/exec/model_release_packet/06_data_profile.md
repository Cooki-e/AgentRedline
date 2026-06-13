# Training and evaluation data profile

Training data:

- Historical completed applications from 2023-01-01 through
  2025-09-30.
- Three pilot-country regions, with strongest representation in metro
  branches.
- Labels based on repayment behavior through first three billing cycles.

Evaluation data:

- Holdout applications from 2025-10-01 through 2026-03-31.
- Evaluation includes the same broad product families as training.

Data notes:

- The training window predates the July 2026 underwriting policy
  update.
- Rural branches and self-employed applicants have lower representation
  than salaried metro applicants.
- Prior-credit-gap applicants have sparse historical signal by design.
- Missing-income records rely on fallback document and account-history
  feature families.
- Historical labels reflect previous queue assignment and branch review
  operations.
