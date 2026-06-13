# completed_project_finch_y1 — archived document 63

Recruitment quarterly summary.

Award: NIH R01-AG056789.

## Detail

Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch.
The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release.
MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance.
Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture.

## Operational notes

- Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain.
- Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending.
- Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff.
- Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive.
- Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck.
- Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key.
- We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.
- We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR.
- The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact.
- MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required.
