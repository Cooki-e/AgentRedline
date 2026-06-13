# completed_project_heron_satellite_y1 — archived document 01

Quarterly progress memo (excerpt).

Award: NIH R01-LM013456.

## Detail

The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004.
The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs.
Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites.
Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.

## Operational notes

- Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004.
- The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday.
- Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged.
- Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP.
- Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance.
- Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission.
- Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment.
- The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter.
- Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only.
- Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.
