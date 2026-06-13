# completed_project_heron_satellite_y1 — archived document 10

Annual NCE narrative justification.

Award: NIH R01-LM013456.

## Detail

Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture.
Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline.
Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending.
Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder.

## Operational notes

- Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release.
- Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged.
- We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.
- The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update.
- Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck.
- Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4.
- Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment.
- MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required.
- Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation.
- The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline.
