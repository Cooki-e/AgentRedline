# completed_project_finch_y1 — archived document 20

Carry-forward request supporting narrative.

Award: NIH R01-AG056789.

## Detail

The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs.
Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge.
Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs.
Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending.

## Operational notes

- Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.
- Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv.
- Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF.
- MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required.
- Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch.
- Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found.
- Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing.
- Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout.
- Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/.
- Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck.
