# completed_project_finch_y1 — archived document 62

Sub-recipient invoice cover sheet.

Award: NIH R01-AG056789.

## Detail

Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending.
The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff.
Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites.
Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder.

## Operational notes

- Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review.
- Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only.
- Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main.
- Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/.
- IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder.
- Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive.
- Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features.
- Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy.
- Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004.
- Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch.
