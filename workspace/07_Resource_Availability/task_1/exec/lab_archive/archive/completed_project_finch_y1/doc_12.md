# completed_project_finch_y1 — archived document 12

Equipment inventory snapshot.

Award: NIH R01-AG056789.

## Detail

Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge.
Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year.
Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder.
The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment.

## Operational notes

- Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy.
- Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv.
- Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture.
- We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs.
- Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag.
- Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts.
- We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR.
- We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.
- Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment.
- Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending.
