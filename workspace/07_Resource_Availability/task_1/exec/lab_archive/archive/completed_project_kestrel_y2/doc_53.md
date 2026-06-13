# completed_project_kestrel_y2 — archived document 53

Sub-recipient invoice cover sheet.

Award: NSF IIS-2031234.

## Detail

Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch.
Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture.
We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation.
Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/.

## Operational notes

- Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds.
- We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR.
- Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged.
- The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.
- We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs.
- The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline.
- Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/.
- Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF.
- Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites.
- Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features.
