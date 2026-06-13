# completed_project_finch_y1 — archived document 49

Quarterly progress memo (excerpt).

Award: NIH R01-AG056789.

## Detail

The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive.
Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending.
Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found.
Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck.

## Operational notes

- Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag.
- Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.
- Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance.
- The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge.
- Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout.
- The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter.
- Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review.
- Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP.
- Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%.
- Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.
