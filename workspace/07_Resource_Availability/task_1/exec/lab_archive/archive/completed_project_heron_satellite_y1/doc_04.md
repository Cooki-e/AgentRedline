# completed_project_heron_satellite_y1 — archived document 04

Site-coordinator monthly check-in notes.

Award: NIH R01-LM013456.

## Detail

Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year.
Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found.
The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint.
Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch.

## Operational notes

- Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%.
- Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive.
- Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged.
- Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv.
- Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag.
- Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy.
- We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.
- The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter.
- Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain.
- Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout.
