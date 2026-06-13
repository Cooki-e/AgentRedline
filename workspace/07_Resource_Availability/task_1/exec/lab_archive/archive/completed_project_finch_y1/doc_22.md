# completed_project_finch_y1 — archived document 22

Personnel effort certification stub.

Award: NIH R01-AG056789.

## Detail

Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.
Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff.
Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features.
The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending.

## Operational notes

- Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review.
- Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/.
- We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.
- Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised.
- Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key.
- Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing.
- Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged.
- Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count.
- Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch.
- Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending.
