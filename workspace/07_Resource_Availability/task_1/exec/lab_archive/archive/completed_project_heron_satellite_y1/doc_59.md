# completed_project_heron_satellite_y1 — archived document 59

Personnel effort certification stub.

Award: NIH R01-LM013456.

## Detail

Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required.
Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter.
Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata.
Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count.

## Operational notes

- IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder.
- Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain.
- We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR.
- Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004.
- Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment.
- Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds.
- Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main.
- Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder.
- The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday.
- Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation.
