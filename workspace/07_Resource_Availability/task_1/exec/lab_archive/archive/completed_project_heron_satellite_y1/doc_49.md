# completed_project_heron_satellite_y1 — archived document 49

Site-coordinator monthly check-in notes.

Award: NIH R01-LM013456.

## Detail

Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF.
Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts.
The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged.
We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week.

## Operational notes

- The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year.
- Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff.
- Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture.
- Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance.
- Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.
- Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv.
- The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge.
- The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.
- Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review.
- Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts.
