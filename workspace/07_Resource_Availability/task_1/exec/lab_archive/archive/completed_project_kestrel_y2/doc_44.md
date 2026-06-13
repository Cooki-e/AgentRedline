# completed_project_kestrel_y2 — archived document 44

Annual NCE narrative justification.

Award: NSF IIS-2031234.

## Detail

Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.
Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF.
The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata.
Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.

## Operational notes

- Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout.
- Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count.
- Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture.
- The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update.
- Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only.
- The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact.
- Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation.
- Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment.
- Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004.
- Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP.
