# completed_project_finch_y1 — archived document 26

Site-coordinator monthly check-in notes.

Award: NIH R01-AG056789.

## Detail

Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment.
MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment.
Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog.
We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%.

## Operational notes

- The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week.
- Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.
- The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge.
- MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required.
- Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review.
- The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint.
- The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year.
- We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs.
- Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.
- Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release.
