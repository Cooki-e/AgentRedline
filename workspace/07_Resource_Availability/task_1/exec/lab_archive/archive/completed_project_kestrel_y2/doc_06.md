# completed_project_kestrel_y2 — archived document 06

Subaward modification memo.

Award: NSF IIS-2031234.

## Detail

Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.
Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation.
Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog.
Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features.

## Operational notes

- Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key.
- Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts.
- Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF.
- Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP.
- The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge.
- The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.
- Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged.
- The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline.
- Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%.
- MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required.
