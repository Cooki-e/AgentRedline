# completed_project_heron_satellite_y1 — archived document 42

Carry-forward request supporting narrative.

Award: NIH R01-LM013456.

## Detail

Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004.
Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder.
Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday.
Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged.

## Operational notes

- Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag.
- We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs.
- Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck.
- Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds.
- Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder.
- We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.
- Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture.
- The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week.
- Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch.
- Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review.
