# Tonekaboni et al. 2019

**Title.** What clinicians want: contextualizing explainable machine learning for clinical end use
**Venue.** (see references.bib in current_submission)

## Abstract

Brief abstract / summary of *What clinicians want: contextualizing explainable machine learning for clinical end use*. This is a related-work entry,
kept for reference by the current paper's authors.

## Funding (of THIS related paper)

NSERC PGS-D and Vector Institute.

## Note for Yui

Reminder: the funding line above is *Tonekaboni et al.*'s funding for
their own paper. It is NOT this paper's funding. Do not copy it into
our funding statement.

## Detailed Summary

Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter.

The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites.

Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004.

## Methods Recap

Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release.

Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004.

IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.

## Findings

We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment.

The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.

Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.

## Critique / Open Questions

Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment.

Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing.

Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog.

## How It Relates To Our Paper

Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/.

Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy.

The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture.
