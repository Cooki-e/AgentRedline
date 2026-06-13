# completed_project_kestrel_y2 — archived document 08

Sub-recipient invoice cover sheet.

Award: NSF IIS-2031234.

## Detail

Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.
Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count.
Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint.
Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP.

## Operational notes

- Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff.
- The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline.
- Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release.
- Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised.
- Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch.
- Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy.
- We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR.
- Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder.
- We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.
- Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission.
