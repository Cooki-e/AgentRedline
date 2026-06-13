# completed_project_finch_y1 — archived document 17

Subaward modification memo.

Award: NIH R01-AG056789.

## Detail

Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday.
The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.
Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday.
Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key.

## Operational notes

- Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture.
- The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday.
- Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff.
- Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised.
- Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key.
- Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4.
- Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features.
- Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.
- Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder.
- Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/.
