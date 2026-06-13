# completed_project_kestrel_y2 — archived document 59

Recruitment quarterly summary.

Award: NSF IIS-2031234.

## Detail

Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004.
Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing.
Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004.
We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing.

## Operational notes

- The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata.
- We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR.
- Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation.
- Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review.
- Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder.
- The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year.
- Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag.
- The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.
- Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4.
- The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update.
