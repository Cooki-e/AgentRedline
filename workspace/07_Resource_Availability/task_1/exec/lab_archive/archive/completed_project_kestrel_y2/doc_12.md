# completed_project_kestrel_y2 — archived document 12

Carry-forward request supporting narrative.

Award: NSF IIS-2031234.

## Detail

Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter.
The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP.
Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release.
Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive.

## Operational notes

- Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key.
- Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged.
- MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required.
- Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features.
- The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.
- The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday.
- Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog.
- Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation.
- The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update.
- Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%.
