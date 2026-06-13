# Robustness and drift checks

Stress slices:

| Slice | AUC | Expected calibration error | Comment |
|---|---:|---:|---|
| Baseline holdout | 0.91 | 0.04 | Overall holdout |
| Missing income field | 0.78 | 0.16 | Income fallback features dominate |
| New employer category | 0.79 | 0.15 | Employer taxonomy changed after 2025Q3 |
| Rural-only branches | 0.82 | 0.11 | Fewer historical examples |
| Post-2025 policy simulation | 0.81 | 0.14 | Applicant mix differs from training window |

Drift watchlist:

- Missing-income applications.
- Employer categories introduced after 2025Q3.
- Branches with low historical representation.
- Applicants with sparse recent credit history.

Evaluation note:

The stress checks do not invalidate the overall AUC result. They show
where the pilot needs monitoring and threshold review because the model
is less stable outside the high-volume slices.
