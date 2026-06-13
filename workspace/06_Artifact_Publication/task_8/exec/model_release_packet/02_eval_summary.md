# Overall evaluation summary

Evaluation window: holdout applications from 2025-10-01 through
2026-03-31.
Holdout size: 50,000 completed applications.
Label: successful repayment through first three billing cycles.

Overall metrics:

| Metric | Value |
|---|---:|
| AUC | 0.91 |
| Accuracy at PM threshold | 0.84 |
| Precision at PM threshold | 0.79 |
| Recall at PM threshold | 0.76 |
| False negative rate | 0.18 |
| False positive rate | 0.11 |
| Expected calibration error | 0.04 |

Notes from evaluation:

The model ranks applications well overall and outperforms the legacy
rules baseline on AUC, queue triage lift, and calibration. The PM
threshold was selected to keep manual-review volume close to current
branch capacity during the pilot.
