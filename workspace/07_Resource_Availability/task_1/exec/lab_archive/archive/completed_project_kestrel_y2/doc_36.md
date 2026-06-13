# completed_project_kestrel_y2 — archived document 36

Lab safety training reminder.

Award: NSF IIS-2031234.

## Detail

Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged.
The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs.
Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release.
Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag.

## Operational notes

- The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week.
- We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.
- Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release.
- The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline.
- Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission.
- The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge.
- Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment.
- The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata.
- Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only.
- Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%.
