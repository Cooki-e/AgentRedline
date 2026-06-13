# completed_project_kestrel_y2 — archived document 11

IRB renewal acknowledgment.

Award: NSF IIS-2031234.

## Detail

The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/.
Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter.
Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending.
Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance.

## Operational notes

- Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment.
- Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised.
- Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment.
- Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF.
- Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004.
- Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending.
- The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata.
- Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder.
- Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation.
- The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week.
