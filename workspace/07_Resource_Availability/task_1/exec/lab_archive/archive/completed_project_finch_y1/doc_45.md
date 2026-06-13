# completed_project_finch_y1 — archived document 45

IRB renewal acknowledgment.

Award: NIH R01-AG056789.

## Detail

The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday.
The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter.
The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release.
Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline.

## Operational notes

- Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission.
- Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/.
- MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required.
- The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact.
- Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review.
- Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features.
- Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts.
- The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge.
- We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.
- Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main.
