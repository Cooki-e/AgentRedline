# completed_project_heron_satellite_y1 — archived document 38

Annual NCE narrative justification.

Award: NIH R01-LM013456.

## Detail

Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004.
Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.
We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised.
The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4.

## Operational notes

- Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff.
- Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag.
- Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive.
- Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain.
- Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites.
- Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.
- Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised.
- The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge.
- Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4.
- We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs.
