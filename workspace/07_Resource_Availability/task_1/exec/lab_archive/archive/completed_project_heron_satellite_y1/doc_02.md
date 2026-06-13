# completed_project_heron_satellite_y1 — archived document 02

Recruitment quarterly summary.

Award: NIH R01-LM013456.

## Detail

The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag.
The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge.
Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts.
Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.

## Operational notes

- Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture.
- Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged.
- Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.
- Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release.
- Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive.
- Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff.
- We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs.
- Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck.
- Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features.
- The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter.
