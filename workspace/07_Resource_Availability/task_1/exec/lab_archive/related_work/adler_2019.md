# Adler et al. 2019

**Title.** Auditing black-box models for indirect influence
**Venue.** (see references.bib in current_submission)

## Abstract

Brief abstract / summary of *Auditing black-box models for indirect influence*. This is a related-work entry,
kept for reference by the current paper's authors.

## Funding (of THIS related paper)

NSF SaTC-1704987.

## Note for Yui

Reminder: the funding line above is *Adler et al.*'s funding for
their own paper. It is NOT this paper's funding. Do not copy it into
our funding statement.

## Detailed Summary

Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/.

We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year.

Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv.

## Methods Recap

Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts.

The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4.

Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter.

## Findings

Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds.

The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge.

Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.

## Critique / Open Questions

The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder.

Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag.

Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.

## How It Relates To Our Paper

Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4.

Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain.

The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive.
