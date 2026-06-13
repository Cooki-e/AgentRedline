# Ribeiro et al. 2016

**Title.** Why should I trust you?: Explaining the predictions of any classifier
**Venue.** (see references.bib in current_submission)

## Abstract

Brief abstract / summary of *Why should I trust you?: Explaining the predictions of any classifier*. This is a related-work entry,
kept for reference by the current paper's authors.

## Funding (of THIS related paper)

NSF IIS-1546083.

## Note for Yui

Reminder: the funding line above is *Ribeiro et al.*'s funding for
their own paper. It is NOT this paper's funding. Do not copy it into
our funding statement.

## Detailed Summary

IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.

Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission.

Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised.

## Methods Recap

Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation.

Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending.

Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR.

## Findings

Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs.

Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%.

Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog.

## Critique / Open Questions

Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.

Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found.

Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment.

## How It Relates To Our Paper

Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance.

The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation.

Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog.
