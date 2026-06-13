# completed_project_kestrel_y2 — archived document 51

Sub-recipient invoice cover sheet.

Award: NSF IIS-2031234.

## Detail

Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy.
Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key.
Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year.
Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.

## Operational notes

- Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/.
- Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck.
- The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday.
- The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter.
- Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised.
- Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy.
- Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.
- The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter.
- Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged.
- Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4.
