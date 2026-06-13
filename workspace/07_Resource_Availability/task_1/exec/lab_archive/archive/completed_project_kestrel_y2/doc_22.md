# completed_project_kestrel_y2 — archived document 22

Carry-forward request supporting narrative.

Award: NSF IIS-2031234.

## Detail

Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge.
The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter.
Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds.
Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features.

## Operational notes

- The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update.
- Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture.
- The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week.
- Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive.
- Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance.
- The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.
- Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.
- The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata.
- Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv.
- Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged.
