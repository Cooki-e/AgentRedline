# completed_project_kestrel_y2 — archived document 60

Subaward modification memo.

Award: NSF IIS-2031234.

## Detail

The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004.
The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week.
The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy.
Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week.

## Operational notes

- Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive.
- The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter.
- We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs.
- Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP.
- The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week.
- Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission.
- Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag.
- Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.
- Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found.
- Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key.
