# completed_project_heron_satellite_y1 — archived document 29

Personnel effort certification stub.

Award: NIH R01-LM013456.

## Detail

Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/.
Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts.
Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata.
MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count.

## Operational notes

- MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required.
- Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending.
- Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP.
- The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update.
- The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline.
- Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key.
- Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment.
- The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint.
- Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff.
- Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main.
