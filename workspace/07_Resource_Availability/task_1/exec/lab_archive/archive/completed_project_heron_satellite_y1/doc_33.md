# completed_project_heron_satellite_y1 — archived document 33

Sub-recipient invoice cover sheet.

Award: NIH R01-LM013456.

## Detail

Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment.
Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update.
Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found.
Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain.

## Operational notes

- Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found.
- Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation.
- Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck.
- Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog.
- The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update.
- We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs.
- Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain.
- The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week.
- Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features.
- The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday.
