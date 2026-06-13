# completed_project_heron_satellite_y1 — archived document 34

Travel reimbursement form (redacted).

Award: NIH R01-LM013456.

## Detail

Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4.
The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment.
Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff.
Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release.

## Operational notes

- Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag.
- Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged.
- IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder.
- Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/.
- Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count.
- Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only.
- The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge.
- Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck.
- Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004.
- The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline.
