# completed_project_finch_y1 — archived document 05

Subaward modification memo.

Award: NIH R01-AG056789.

## Detail

The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain.
IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder.
Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update.
IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.

## Operational notes

- Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4.
- The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata.
- Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts.
- Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv.
- Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features.
- Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main.
- Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder.
- Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds.
- Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%.
- Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck.
