# completed_project_kestrel_y2 — archived document 20

IRB renewal acknowledgment.

Award: NSF IIS-2031234.

## Detail

Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission.
Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact.
Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main.
Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required.

## Operational notes

- Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/.
- Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy.
- Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment.
- Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.
- Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key.
- Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.
- The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter.
- We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.
- Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP.
- Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck.
