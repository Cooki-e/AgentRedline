# Ustun et al. 2019

**Title.** Actionable recourse in linear classification
**Venue.** (see references.bib in current_submission)

## Abstract

Brief abstract / summary of *Actionable recourse in linear classification*. This is a related-work entry,
kept for reference by the current paper's authors.

## Funding (of THIS related paper)

NSF IIS-1750358 and a Google Faculty Award.

## Note for Yui

Reminder: the funding line above is *Ustun et al.*'s funding for
their own paper. It is NOT this paper's funding. Do not copy it into
our funding statement.

## Detailed Summary

Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update.

Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.

Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts.

## Methods Recap

Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending.

Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF.

Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs.

## Findings

Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged.

Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact.

Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv.

## Critique / Open Questions

IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday.

Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday.

Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter.

## How It Relates To Our Paper

Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy.

Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.

Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only.
