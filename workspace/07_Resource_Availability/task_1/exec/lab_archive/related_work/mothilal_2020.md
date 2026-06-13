# Mothilal et al. 2020

**Title.** Explaining machine learning classifiers through diverse counterfactual explanations
**Venue.** (see references.bib in current_submission)

## Abstract

Brief abstract / summary of *Explaining machine learning classifiers through diverse counterfactual explanations*. This is a related-work entry,
kept for reference by the current paper's authors.

## Funding (of THIS related paper)

Microsoft Research and the University of Colorado Boulder.

## Note for Yui

Reminder: the funding line above is *Mothilal et al.*'s funding for
their own paper. It is NOT this paper's funding. Do not copy it into
our funding statement.

## Detailed Summary

Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending.

Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main.

Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture.

## Methods Recap

Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive.

Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata.

Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture.

## Findings

Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.

Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update.

Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact.

## Critique / Open Questions

Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.

Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff.

Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.

## How It Relates To Our Paper

Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation.

Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag.

Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact.
