# completed_project_kestrel_y2 — archived document 34

IRB renewal acknowledgment.

Award: NSF IIS-2031234.

## Detail

Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter.
We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing.
Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week.
Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only.

## Operational notes

- Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending.
- Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites.
- Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found.
- Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts.
- Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key.
- The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint.
- Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder.
- Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004.
- The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.
- Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF.
