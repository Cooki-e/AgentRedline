# completed_project_finch_y1 — archived document 15

Recruitment quarterly summary.

Award: NIH R01-AG056789.

## Detail

Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key.
Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP.
We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance.
Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint.

## Operational notes

- Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.
- The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge.
- Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment.
- Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy.
- Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing.
- Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged.
- IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder.
- The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata.
- The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint.
- Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/.
