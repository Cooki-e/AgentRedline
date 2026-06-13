# completed_project_finch_y1 — archived document 14

Lab safety training reminder.

Award: NIH R01-AG056789.

## Detail

Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing.
Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP.
Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count.
Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff.

## Operational notes

- We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs.
- Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog.
- Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds.
- The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year.
- The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint.
- We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.
- Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff.
- Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.
- Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features.
- Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout.
