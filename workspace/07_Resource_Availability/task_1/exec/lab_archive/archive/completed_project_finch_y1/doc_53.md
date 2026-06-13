# completed_project_finch_y1 — archived document 53

Personnel effort certification stub.

Award: NIH R01-AG056789.

## Detail

Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%.
The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck.
Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive.
Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday.

## Operational notes

- The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge.
- We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR.
- Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review.
- Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count.
- Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing.
- Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv.
- The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint.
- The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday.
- IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder.
- Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged.
