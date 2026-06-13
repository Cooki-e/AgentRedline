# completed_project_kestrel_y2 — archived document 43

Lab safety training reminder.

Award: NSF IIS-2031234.

## Detail

Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found.
Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4.
Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag.
Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata.

## Operational notes

- Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy.
- The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact.
- Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff.
- Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch.
- Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive.
- IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder.
- Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.
- Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending.
- Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation.
- Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised.
