# completed_project_finch_y1 — archived document 33

Annual NCE narrative justification.

Award: NIH R01-AG056789.

## Detail

Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004.
Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP.
Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged.
Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag.

## Operational notes

- Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag.
- We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.
- Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy.
- Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features.
- The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week.
- The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update.
- We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR.
- The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge.
- Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found.
- Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture.
