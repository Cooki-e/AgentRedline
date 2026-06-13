# completed_project_heron_satellite_y1 — archived document 40

IRB renewal acknowledgment.

Award: NIH R01-LM013456.

## Detail

Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive.
Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.
The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs.
The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds.

## Operational notes

- Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.
- Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch.
- The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint.
- The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update.
- Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture.
- Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment.
- Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts.
- Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance.
- Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder.
- Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key.
