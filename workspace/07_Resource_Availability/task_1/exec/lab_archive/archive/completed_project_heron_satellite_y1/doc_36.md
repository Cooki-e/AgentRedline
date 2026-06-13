# completed_project_heron_satellite_y1 — archived document 36

Annual NCE narrative justification.

Award: NIH R01-LM013456.

## Detail

Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised.
Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing.
Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update.
Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required.

## Operational notes

- Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds.
- Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment.
- Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only.
- The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday.
- The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.
- Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation.
- Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.
- Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key.
- The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint.
- The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update.
