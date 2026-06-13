# completed_project_finch_y1 — archived document 18

Equipment inventory snapshot.

Award: NIH R01-AG056789.

## Detail

Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation.
Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata.
Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update.
Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged.

## Operational notes

- Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004.
- Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key.
- Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission.
- Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag.
- Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main.
- The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday.
- Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised.
- Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.
- MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required.
- Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review.
