# completed_project_finch_y1 — archived document 42

IRB renewal acknowledgment.

Award: NIH R01-AG056789.

## Detail

The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy.
Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck.
Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending.
We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact.

## Operational notes

- The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week.
- Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features.
- The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata.
- Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004.
- Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.
- Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv.
- Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts.
- Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck.
- Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff.
- The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update.
