# completed_project_finch_y1 — archived document 23

Sub-recipient invoice cover sheet.

Award: NIH R01-AG056789.

## Detail

The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts.
Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata.
The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.
The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata.

## Operational notes

- Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main.
- MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required.
- Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found.
- Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review.
- The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact.
- Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004.
- The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update.
- Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%.
- Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment.
- IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder.
