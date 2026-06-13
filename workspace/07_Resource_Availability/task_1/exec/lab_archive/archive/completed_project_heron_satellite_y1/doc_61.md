# completed_project_heron_satellite_y1 — archived document 61

Recruitment quarterly summary.

Award: NIH R01-LM013456.

## Detail

Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff.
The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch.
Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count.
Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release.

## Operational notes

- Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged.
- Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch.
- The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata.
- The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday.
- Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.
- Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission.
- Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing.
- IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder.
- Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004.
- The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter.
