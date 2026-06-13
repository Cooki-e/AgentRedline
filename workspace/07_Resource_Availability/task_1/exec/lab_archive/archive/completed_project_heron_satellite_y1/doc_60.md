# completed_project_heron_satellite_y1 — archived document 60

Carry-forward request supporting narrative.

Award: NIH R01-LM013456.

## Detail

Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week.
Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog.
The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout.
Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review.

## Operational notes

- Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main.
- Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count.
- Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4.
- Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found.
- Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment.
- The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week.
- The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter.
- Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds.
- IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder.
- Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch.
