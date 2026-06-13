# completed_project_finch_y1 — archived document 24

Site-coordinator monthly check-in notes.

Award: NIH R01-AG056789.

## Detail

Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata.
Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy.
The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag.
MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.

## Operational notes

- Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck.
- Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features.
- IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder.
- The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata.
- Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF.
- Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog.
- Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv.
- Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds.
- The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter.
- MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required.
