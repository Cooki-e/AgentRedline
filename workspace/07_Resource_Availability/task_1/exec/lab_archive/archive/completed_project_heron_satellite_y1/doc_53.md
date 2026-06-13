# completed_project_heron_satellite_y1 — archived document 53

IRB renewal acknowledgment.

Award: NIH R01-LM013456.

## Detail

Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck.
We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv.
Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.
Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment.

## Operational notes

- Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck.
- Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing.
- The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday.
- Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch.
- The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter.
- Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%.
- The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint.
- Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count.
- Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag.
- IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder.
