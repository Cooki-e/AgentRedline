# completed_project_finch_y1 — archived document 21

Travel reimbursement form (redacted).

Award: NIH R01-AG056789.

## Detail

The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.
Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint.
Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.
We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck.

## Operational notes

- The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata.
- The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge.
- The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday.
- The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter.
- Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder.
- Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment.
- Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing.
- Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag.
- We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.
- Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff.
