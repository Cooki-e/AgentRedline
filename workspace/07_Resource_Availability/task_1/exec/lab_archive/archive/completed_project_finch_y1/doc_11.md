# completed_project_finch_y1 — archived document 11

Personnel effort certification stub.

Award: NIH R01-AG056789.

## Detail

Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key.
Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder.
We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main.
Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features.

## Operational notes

- We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs.
- Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised.
- We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR.
- Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff.
- Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck.
- IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder.
- Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing.
- Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending.
- Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog.
- Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004.
