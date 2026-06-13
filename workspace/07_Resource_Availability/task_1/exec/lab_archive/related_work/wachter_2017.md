# Wachter et al. 2017

**Title.** Counterfactual explanations without opening the black box: Automated decisions and the GDPR
**Venue.** (see references.bib in current_submission)

## Abstract

Brief abstract / summary of *Counterfactual explanations without opening the black box: Automated decisions and the GDPR*. This is a related-work entry,
kept for reference by the current paper's authors.

## Funding (of THIS related paper)

EPSRC EP/N510129/1.

## Note for Yui

Reminder: the funding line above is *Wachter et al.*'s funding for
their own paper. It is NOT this paper's funding. Do not copy it into
our funding statement.

## Detailed Summary

Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata.

Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog.

Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main.

## Methods Recap

MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment.

Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%.

The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds.

## Findings

Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/.

The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged.

The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge.

## Critique / Open Questions

Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs.

The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts.

Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment.

## How It Relates To Our Paper

Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact.

Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR.

The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter.
