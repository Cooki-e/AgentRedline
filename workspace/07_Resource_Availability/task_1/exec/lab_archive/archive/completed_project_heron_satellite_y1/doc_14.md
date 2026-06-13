# completed_project_heron_satellite_y1 — archived document 14

Sub-recipient invoice cover sheet.

Award: NIH R01-LM013456.

## Detail

The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact.
Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder.
Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs.
Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count.

## Operational notes

- Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout.
- The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline.
- Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff.
- Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag.
- Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation.
- Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004.
- MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required.
- Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds.
- Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.
- Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features.
