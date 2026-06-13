# completed_project_kestrel_y2 — archived document 29

Travel reimbursement form (redacted).

Award: NSF IIS-2031234.

## Detail

IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck.
The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update.
Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only.
Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter.

## Operational notes

- Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout.
- The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact.
- Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture.
- Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy.
- Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features.
- Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending.
- Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main.
- We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.
- Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag.
- MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required.
