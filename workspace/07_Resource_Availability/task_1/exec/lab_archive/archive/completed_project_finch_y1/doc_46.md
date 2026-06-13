# completed_project_finch_y1 — archived document 46

Equipment inventory snapshot.

Award: NIH R01-AG056789.

## Detail

Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance.
Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive.
Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features.
Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.

## Operational notes

- Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch.
- Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review.
- Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004.
- Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%.
- Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy.
- Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv.
- Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised.
- We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.
- Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds.
- The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.
