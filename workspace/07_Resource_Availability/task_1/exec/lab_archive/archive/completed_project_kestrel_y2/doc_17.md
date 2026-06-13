# completed_project_kestrel_y2 — archived document 17

Subaward modification memo.

Award: NSF IIS-2031234.

## Detail

Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review.
Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff.
Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count.
Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged.

## Operational notes

- Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found.
- The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week.
- Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only.
- Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged.
- Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%.
- The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge.
- The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday.
- The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact.
- We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR.
- Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending.
