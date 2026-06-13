# completed_project_finch_y1 — archived document 06

IRB renewal acknowledgment.

Award: NIH R01-AG056789.

## Detail

Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive.
The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing.
The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag.
Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline.

## Operational notes

- IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder.
- The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline.
- Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission.
- Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.
- The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year.
- Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder.
- Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/.
- Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv.
- The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter.
- The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint.
