# completed_project_kestrel_y2 — archived document 63

Lab safety training reminder.

Award: NSF IIS-2031234.

## Detail

The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required.
Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday.
Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR.
The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact.

## Operational notes

- Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%.
- Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain.
- Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv.
- Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture.
- We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.
- The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.
- Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment.
- The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline.
- Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds.
- Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance.
