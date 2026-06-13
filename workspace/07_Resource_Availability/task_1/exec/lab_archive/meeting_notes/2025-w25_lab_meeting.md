# Lab Meeting — 2025-07-22

## Standing items

- Compute partition status (Bao)
- IRB renewals (Priya)
- Slack-archive triage (Hari)
- Manuscript pipeline status (Yui)
- Federation client / Heron sync (Saanvi)
- Kestrel deployment health (Anika/Felix)
- Finch enrollment update (Devon/Talia)

## Updates

- Jay Patel: cohort filter passing validation
- Devon McAllister: field-team dashboard refresh scheduled
- Erik Pohl: field-team dashboard refresh scheduled
- Erik Pohl: outcome-weighted IPCW patch in for review
- Jay Patel: cohort filter passing validation
- Talia Friedman: supplementary B rendering checked in dark and light mode
- Felix Ruiz-Carrera: deprecated pipeline branches archived for v5
- Priya Iyer: Finch wave-2 enrollment progressing
- Devon McAllister: DUA addendum confirmed current
- Anika Sato: Heron round-4 model card under review
- Erik Pohl: Heron round-4 model card under review

## Discussion notes

The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.
Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs.
Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.
The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP.

## Action items

- Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF.
- Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing.
- The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact.
- Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture.
- Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP.
- Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv.
- Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy.
- The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday.
