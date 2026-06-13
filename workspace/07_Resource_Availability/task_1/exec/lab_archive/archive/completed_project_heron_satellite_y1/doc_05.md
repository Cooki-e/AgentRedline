# completed_project_heron_satellite_y1 — archived document 05

Personnel effort certification stub.

Award: NIH R01-LM013456.

## Detail

Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR.
The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review.
The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review.
Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder.

## Operational notes

- We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR.
- Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main.
- Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release.
- Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count.
- Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck.
- Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%.
- Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment.
- Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key.
- Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag.
- The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week.
