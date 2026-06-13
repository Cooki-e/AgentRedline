# completed_project_kestrel_y2 — archived document 32

Equipment inventory snapshot.

Award: NSF IIS-2031234.

## Detail

Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.
Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy.
Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.
Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds.

## Operational notes

- Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance.
- Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff.
- We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.
- Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog.
- The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday.
- Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing.
- Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features.
- The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year.
- Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive.
- Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds.
