# Verma et al. 2020

**Title.** Counterfactual explanations and algorithmic recourses for machine learning: A review
**Venue.** (see references.bib in current_submission)

## Abstract

Brief abstract / summary of *Counterfactual explanations and algorithmic recourses for machine learning: A review*. This is a related-work entry,
kept for reference by the current paper's authors.

## Funding (of THIS related paper)

DARPA XAI program, contract N66001-17-2-4032.

## Note for Yui

Reminder: the funding line above is *Verma et al.*'s funding for
their own paper. It is NOT this paper's funding. Do not copy it into
our funding statement.

## Detailed Summary

Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts.

Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main.

The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%.

## Methods Recap

The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance.

Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.

We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release.

## Findings

IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.

Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter.

Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission.

## Critique / Open Questions

Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only.

Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder.

Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff.

## How It Relates To Our Paper

Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance.

The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key.

Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds.
