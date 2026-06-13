# completed_project_heron_satellite_y1 — archived document 09

Subaward modification memo.

Award: NIH R01-LM013456.

## Detail

Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder.
Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised.
Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag.
Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder.

## Operational notes

- Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised.
- Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only.
- The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter.
- Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004.
- Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag.
- Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found.
- The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline.
- Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.
- Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release.
- Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv.
