# completed_project_finch_y1 — archived document 57

IRB renewal acknowledgment.

Award: NIH R01-AG056789.

## Detail

Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending.
The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch.
MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch.
Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review.

## Operational notes

- Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/.
- Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.
- The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint.
- Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending.
- Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4.
- Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key.
- Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count.
- Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF.
- Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged.
- We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR.
