# completed_project_heron_satellite_y1 — archived document 31

Sub-recipient invoice cover sheet.

Award: NIH R01-LM013456.

## Detail

We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv.
Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance.
Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff.
The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.

## Operational notes

- Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy.
- Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only.
- The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline.
- Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch.
- Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%.
- Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review.
- MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required.
- Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release.
- Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites.
- Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF.
