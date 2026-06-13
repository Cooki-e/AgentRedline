# completed_project_kestrel_y2 — archived document 48

Quarterly progress memo (excerpt).

Award: NSF IIS-2031234.

## Detail

Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog.
Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag.
Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004.
Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact.

## Operational notes

- The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata.
- Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture.
- The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday.
- Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%.
- Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy.
- Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending.
- The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.
- Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/.
- Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing.
- Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised.
