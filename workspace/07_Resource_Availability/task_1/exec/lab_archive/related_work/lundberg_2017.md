# Lundberg et al. 2017

**Title.** A unified approach to interpreting model predictions
**Venue.** (see references.bib in current_submission)

## Abstract

Brief abstract / summary of *A unified approach to interpreting model predictions*. This is a related-work entry,
kept for reference by the current paper's authors.

## Funding (of THIS related paper)

NIH F31-CA192556.

## Note for Yui

Reminder: the funding line above is *Lundberg et al.*'s funding for
their own paper. It is NOT this paper's funding. Do not copy it into
our funding statement.

## Detailed Summary

Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/.

Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing.

Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.

## Methods Recap

The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised.

Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.

Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive.

## Findings

Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy.

Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact.

Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter.

## Critique / Open Questions

The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.

Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance.

Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact.

## How It Relates To Our Paper

Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv.

The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline.

The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004.
