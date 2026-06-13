# completed_project_finch_y1 — archived document 36

Travel reimbursement form (redacted).

Award: NIH R01-AG056789.

## Detail

The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday.
Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.
Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs.
Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint.

## Operational notes

- Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP.
- Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending.
- The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter.
- The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline.
- Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog.
- The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter.
- Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv.
- We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs.
- Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review.
- Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged.
