# completed_project_heron_satellite_y1 — archived document 23

Equipment inventory snapshot.

Award: NIH R01-LM013456.

## Detail

We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline.
Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.
Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain.
Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending.

## Operational notes

- Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.
- Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder.
- Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004.
- Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing.
- Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance.
- Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds.
- Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4.
- Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts.
- The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter.
- The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint.
