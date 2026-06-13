# completed_project_heron_satellite_y1 — archived document 39

IRB renewal acknowledgment.

Award: NIH R01-LM013456.

## Detail

Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts.
Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter.
Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP.
Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update.

## Operational notes

- MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required.
- Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation.
- We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR.
- Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv.
- Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review.
- Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck.
- Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture.
- Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder.
- The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter.
- We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.
