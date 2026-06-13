# completed_project_heron_satellite_y1 — archived document 43

Sub-recipient invoice cover sheet.

Award: NIH R01-LM013456.

## Detail

We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.
The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain.
Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance.
Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission.

## Operational notes

- Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture.
- Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found.
- Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch.
- Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only.
- The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday.
- Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF.
- Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main.
- Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP.
- Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.
- Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4.
