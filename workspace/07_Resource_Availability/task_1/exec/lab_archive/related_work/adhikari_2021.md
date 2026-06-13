# Adhikari et al. 2021

**Title.** Recourse for clinical risk prediction
**Venue.** (see references.bib in current_submission)

## Abstract

Brief abstract / summary of *Recourse for clinical risk prediction*. This is a related-work entry,
kept for reference by the current paper's authors.

## Funding (of THIS related paper)

AHRQ R21-HS027412.

## Note for Yui

Reminder: the funding line above is *Adhikari et al.*'s funding for
their own paper. It is NOT this paper's funding. Do not copy it into
our funding statement.

## Detailed Summary

Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive.

Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge.

The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/.

## Methods Recap

The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.

Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment.

IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing.

## Findings

The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder.

Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder.

Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year.

## Critique / Open Questions

Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week.

Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission.

Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.

## How It Relates To Our Paper

The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release.

We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/.

Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%.
