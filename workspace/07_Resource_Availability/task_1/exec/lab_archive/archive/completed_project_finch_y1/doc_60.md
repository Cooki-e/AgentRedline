# completed_project_finch_y1 — archived document 60

Sub-recipient invoice cover sheet.

Award: NIH R01-AG056789.

## Detail

Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/.
Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.
Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review.
MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog.

## Operational notes

- Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features.
- Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release.
- Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites.
- The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact.
- The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline.
- The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.
- Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/.
- The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week.
- Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy.
- Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing.
