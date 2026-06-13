# completed_project_kestrel_y2 — archived document 25

Lab safety training reminder.

Award: NSF IIS-2031234.

## Detail

Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment.
Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key.
We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck.
Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.

## Operational notes

- Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment.
- Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog.
- Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv.
- Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment.
- Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key.
- Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing.
- The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.
- Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.
- Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck.
- Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts.
