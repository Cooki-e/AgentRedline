# completed_project_finch_y1 — archived document 34

Equipment inventory snapshot.

Award: NIH R01-AG056789.

## Detail

Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge.
Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch.
The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck.
The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint.

## Operational notes

- Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment.
- The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact.
- Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv.
- Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.
- We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs.
- Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised.
- Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy.
- We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR.
- Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4.
- The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter.
