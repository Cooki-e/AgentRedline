# completed_project_heron_satellite_y1 — archived document 57

Annual NCE narrative justification.

Award: NIH R01-LM013456.

## Detail

The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update.
We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found.
Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%.
The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture.

## Operational notes

- MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required.
- The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge.
- Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found.
- Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites.
- Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment.
- Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features.
- The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.
- Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4.
- The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year.
- The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint.
