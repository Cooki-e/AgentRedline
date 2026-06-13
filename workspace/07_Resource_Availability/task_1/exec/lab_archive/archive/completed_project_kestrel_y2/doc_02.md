# completed_project_kestrel_y2 — archived document 02

Recruitment quarterly summary.

Award: NSF IIS-2031234.

## Detail

Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation.
The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%.
The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs.
We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count.

## Operational notes

- Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch.
- Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.
- Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004.
- Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only.
- Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.
- Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment.
- The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint.
- The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact.
- Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout.
- Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy.
