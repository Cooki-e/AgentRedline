# completed_project_kestrel_y2 — archived document 18

Quarterly progress memo (excerpt).

Award: NSF IIS-2031234.

## Detail

The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features.
Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder.
The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata.
Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR.

## Operational notes

- Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged.
- Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission.
- Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment.
- Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.
- The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.
- Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key.
- Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review.
- Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release.
- Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features.
- The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter.
