# VanLooveren et al. 2021

**Title.** Interpretable counterfactual explanations guided by prototypes
**Venue.** (see references.bib in current_submission)

## Abstract

Brief abstract / summary of *Interpretable counterfactual explanations guided by prototypes*. This is a related-work entry,
kept for reference by the current paper's authors.

## Funding (of THIS related paper)

Seldon Technologies internal R&D.

## Note for Yui

Reminder: the funding line above is *VanLooveren et al.*'s funding for
their own paper. It is NOT this paper's funding. Do not copy it into
our funding statement.

## Detailed Summary

The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment.

The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP.

Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main.

## Methods Recap

Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv.

Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture.

The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF.

## Findings

Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge.

Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features.

We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.

## Critique / Open Questions

Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog.

Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission.

Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year.

## How It Relates To Our Paper

Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged.

Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder.

IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment.
