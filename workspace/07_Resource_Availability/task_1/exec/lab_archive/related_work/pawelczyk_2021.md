# Pawelczyk et al. 2021

**Title.** CARLA: A Python library to benchmark algorithmic recourse and counterfactual explanation algorithms
**Venue.** (see references.bib in current_submission)

## Abstract

Brief abstract / summary of *CARLA: A Python library to benchmark algorithmic recourse and counterfactual explanation algorithms*. This is a related-work entry,
kept for reference by the current paper's authors.

## Funding (of THIS related paper)

DFG (Deutsche Forschungsgemeinschaft) project KA 4520/1.

## Note for Yui

Reminder: the funding line above is *Pawelczyk et al.*'s funding for
their own paper. It is NOT this paper's funding. Do not copy it into
our funding statement.

## Detailed Summary

The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features.

MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds.

MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog.

## Methods Recap

Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features.

Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.

We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance.

## Findings

The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance.

The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review.

Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog.

## Critique / Open Questions

Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main.

Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.

Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004.

## How It Relates To Our Paper

The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts.

Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs.

Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review.
