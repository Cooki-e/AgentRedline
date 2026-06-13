# completed_project_heron_satellite_y1 — archived document 12

Travel reimbursement form (redacted).

Award: NIH R01-LM013456.

## Detail

Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment.
Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts.
Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.
The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004.

## Operational notes

- Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features.
- Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment.
- The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter.
- We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR.
- Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment.
- Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv.
- Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff.
- Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag.
- Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count.
- Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release.
