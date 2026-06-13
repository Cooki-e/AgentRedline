# completed_project_heron_satellite_y1 — archived document 62

Equipment inventory snapshot.

Award: NIH R01-LM013456.

## Detail

Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge.
Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features.
Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain.
Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday.

## Operational notes

- The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint.
- The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact.
- Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged.
- Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment.
- Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff.
- Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP.
- Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review.
- We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.
- Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites.
- Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch.
