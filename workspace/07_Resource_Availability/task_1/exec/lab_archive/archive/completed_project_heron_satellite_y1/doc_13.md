# completed_project_heron_satellite_y1 — archived document 13

Recruitment quarterly summary.

Award: NIH R01-LM013456.

## Detail

Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain.
Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/.
The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata.
The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder.

## Operational notes

- The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint.
- Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending.
- We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.
- Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF.
- Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main.
- The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.
- IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder.
- Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only.
- Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4.
- Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch.
