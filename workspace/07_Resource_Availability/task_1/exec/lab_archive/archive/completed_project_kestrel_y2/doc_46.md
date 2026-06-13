# completed_project_kestrel_y2 — archived document 46

Site-coordinator monthly check-in notes.

Award: NSF IIS-2031234.

## Detail

Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive.
Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.
The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline.
Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4.

## Operational notes

- Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release.
- Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv.
- Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key.
- The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint.
- Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised.
- Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%.
- Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP.
- Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF.
- Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment.
- We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs.
