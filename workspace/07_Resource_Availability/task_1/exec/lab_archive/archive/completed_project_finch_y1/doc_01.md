# completed_project_finch_y1 — archived document 01

Carry-forward request supporting narrative.

Award: NIH R01-AG056789.

## Detail

Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter.
Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.
Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only.
Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata.

## Operational notes

- Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count.
- The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday.
- Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck.
- Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts.
- The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint.
- Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv.
- Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds.
- Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review.
- The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge.
- Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment.
