# completed_project_finch_y1 — archived document 39

Personnel effort certification stub.

Award: NIH R01-AG056789.

## Detail

The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata.
Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog.
The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts.
Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing.

## Operational notes

- Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy.
- Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features.
- Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds.
- Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing.
- Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key.
- Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only.
- The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.
- MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required.
- Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission.
- The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update.
