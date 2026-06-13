# Poyiadzi et al. 2020

**Title.** FACE: Feasible and actionable counterfactual explanations
**Venue.** (see references.bib in current_submission)

## Abstract

Brief abstract / summary of *FACE: Feasible and actionable counterfactual explanations*. This is a related-work entry,
kept for reference by the current paper's authors.

## Funding (of THIS related paper)

EPSRC Centre for Doctoral Training EP/L016516/1.

## Note for Yui

Reminder: the funding line above is *Poyiadzi et al.*'s funding for
their own paper. It is NOT this paper's funding. Do not copy it into
our funding statement.

## Detailed Summary

Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge.

Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline.

The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.

## Methods Recap

Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.

The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation.

Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive.

## Findings

Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year.

We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint.

Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%.

## Critique / Open Questions

Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance.

The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder.

We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter.

## How It Relates To Our Paper

The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update.

The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint.

Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment.
