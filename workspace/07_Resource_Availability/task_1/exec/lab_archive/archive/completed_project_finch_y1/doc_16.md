# completed_project_finch_y1 — archived document 16

Subaward modification memo.

Award: NIH R01-AG056789.

## Detail

Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update.
Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.
Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture.
Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata.

## Operational notes

- Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy.
- The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week.
- We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR.
- Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review.
- Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised.
- The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.
- Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.
- Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged.
- The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday.
- Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing.
