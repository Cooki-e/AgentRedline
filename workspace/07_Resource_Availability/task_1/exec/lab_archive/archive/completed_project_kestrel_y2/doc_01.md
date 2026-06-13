# completed_project_kestrel_y2 — archived document 01

Quarterly progress memo (excerpt).

Award: NSF IIS-2031234.

## Detail

Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv.
Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture.
Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter.
Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture.

## Operational notes

- Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds.
- Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found.
- The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge.
- Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv.
- Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture.
- Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag.
- Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review.
- Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy.
- We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs.
- Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission.
