# completed_project_kestrel_y2 — archived document 39

IRB renewal acknowledgment.

Award: NSF IIS-2031234.

## Detail

The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds.
The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4.
Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/.
Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release.

## Operational notes

- Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised.
- Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout.
- The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata.
- The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter.
- Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF.
- Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff.
- The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter.
- Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation.
- MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required.
- Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck.
