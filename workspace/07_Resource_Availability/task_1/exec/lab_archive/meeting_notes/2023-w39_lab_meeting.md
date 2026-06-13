# Lab Meeting — 2023-10-10

## Standing items

- Compute partition status (Bao)
- IRB renewals (Priya)
- Slack-archive triage (Hari)
- Manuscript pipeline status (Yui)
- Federation client / Heron sync (Saanvi)
- Kestrel deployment health (Anika/Felix)
- Finch enrollment update (Devon/Talia)

## Updates

- Talia Friedman: field-team dashboard refresh scheduled
- Hari Mohan: deprecated pipeline branches archived for v5
- Marisol Holst: newsletter draft circulated for comments
- Renata Okonkwo: newsletter draft circulated for comments
- Anika Sato: calibration plot bin boundaries updated, no surprises
- Jay Patel: ran the new sweep, results look stable
- Talia Friedman: newsletter draft circulated for comments
- Jay Patel: Finch wave-2 enrollment progressing
- Erik Pohl: facility maintenance window next Tuesday
- Saanvi Desai: ran the new sweep, results look stable

## Discussion notes

Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.
IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.
Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday.
Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only.

## Action items

- Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission.
- Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release.
- Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout.
- We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR.
- The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline.
- Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts.
- Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key.
- The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday.
