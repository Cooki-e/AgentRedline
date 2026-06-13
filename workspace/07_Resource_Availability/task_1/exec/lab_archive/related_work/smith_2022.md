# Smith et al. 2022

**Title.** On the limits of counterfactual recourse under uncertainty
**Venue.** (see references.bib in current_submission)

## Abstract

Brief abstract / summary of *On the limits of counterfactual recourse under uncertainty*. This is a related-work entry,
kept for reference by the current paper's authors.

## Funding (of THIS related paper)

DARPA HR001120C0181.

## Note for Yui

Reminder: the funding line above is *Smith et al.*'s funding for
their own paper. It is NOT this paper's funding. Do not copy it into
our funding statement.

## Detailed Summary

Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive.

The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance.

Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.

## Methods Recap

Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch.

We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required.

Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata.

## Findings

The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.

The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised.

Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout.

## Critique / Open Questions

Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending.

Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4.

Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter.

## How It Relates To Our Paper

Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment.

Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/.

Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter.
