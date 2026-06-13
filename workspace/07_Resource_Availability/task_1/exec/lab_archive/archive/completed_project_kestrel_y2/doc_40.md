# completed_project_kestrel_y2 — archived document 40

IRB renewal acknowledgment.

Award: NSF IIS-2031234.

## Detail

Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key.
Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck.
Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter.
Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment.

## Operational notes

- Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending.
- Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation.
- Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy.
- The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.
- The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline.
- We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR.
- Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release.
- Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder.
- Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only.
- Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF.
