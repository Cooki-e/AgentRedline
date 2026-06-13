# completed_project_kestrel_y2 — archived document 33

IRB renewal acknowledgment.

Award: NSF IIS-2031234.

## Detail

Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.
The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised.
Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint.
The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.

## Operational notes

- The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year.
- Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag.
- Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count.
- The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge.
- Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment.
- Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF.
- Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release.
- Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised.
- Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv.
- The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata.
