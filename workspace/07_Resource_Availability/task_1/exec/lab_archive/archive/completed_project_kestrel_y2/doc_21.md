# completed_project_kestrel_y2 — archived document 21

Site-coordinator monthly check-in notes.

Award: NSF IIS-2031234.

## Detail

Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch.
Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag.
Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture.
The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday.

## Operational notes

- Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release.
- Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout.
- Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.
- Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain.
- Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only.
- The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter.
- Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff.
- Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog.
- Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending.
- Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004.
