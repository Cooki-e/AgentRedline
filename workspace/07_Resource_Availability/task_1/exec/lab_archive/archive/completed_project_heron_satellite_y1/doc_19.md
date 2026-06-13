# completed_project_heron_satellite_y1 — archived document 19

Quarterly progress memo (excerpt).

Award: NIH R01-LM013456.

## Detail

Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge.
Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder.
The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder.
Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog.

## Operational notes

- Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive.
- We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.
- Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main.
- Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites.
- The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday.
- The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata.
- Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts.
- The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.
- Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag.
- Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder.
