# Karimi et al. 2020

**Title.** Model-agnostic counterfactual explanations for consequential decisions
**Venue.** (see references.bib in current_submission)

## Abstract

Brief abstract / summary of *Model-agnostic counterfactual explanations for consequential decisions*. This is a related-work entry,
kept for reference by the current paper's authors.

## Funding (of THIS related paper)

Max Planck Society.

## Note for Yui

Reminder: the funding line above is *Karimi et al.*'s funding for
their own paper. It is NOT this paper's funding. Do not copy it into
our funding statement.

## Detailed Summary

The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter.

The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain.

Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch.

## Methods Recap

The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main.

Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder.

The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.

## Findings

Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update.

Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.

Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout.

## Critique / Open Questions

Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog.

Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance.

Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain.

## How It Relates To Our Paper

Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.

Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder.

Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag.
