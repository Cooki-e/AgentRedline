# Lab Meeting — 2025-03-01

## Standing items

- Compute partition status (Bao)
- IRB renewals (Priya)
- Slack-archive triage (Hari)
- Manuscript pipeline status (Yui)
- Federation client / Heron sync (Saanvi)
- Kestrel deployment health (Anika/Felix)
- Finch enrollment update (Devon/Talia)

## Updates

- Erik Pohl: Kestrel sensor pull came in
- Erik Pohl: calibration plot bin boundaries updated, no surprises
- Hari Mohan: Finch wave-2 enrollment progressing
- Saanvi Desai: Finch wave-2 enrollment progressing
- Saanvi Desai: Finch wave-2 enrollment progressing
- Anika Sato: Felix's sensor pull script PR is up
- Yui Tanaka: DUA addendum confirmed current
- Priya Iyer: newsletter draft circulated for comments
- Devon McAllister: field-team dashboard refresh scheduled
- Bao Nguyen: ran the new sweep, results look stable
- Renata Okonkwo: facility maintenance window next Tuesday
- Yui Tanaka: newsletter draft circulated for comments
- Talia Friedman: newsletter draft circulated for comments
- Saanvi Desai: JBI revision continues, funding section still on Jay
- Renata Okonkwo: facility maintenance window next Tuesday
- Hari Mohan: cohort filter passing validation
- Devon McAllister: DUA addendum confirmed current
- Marisol Holst: supplementary B rendering checked in dark and light mode

## Discussion notes

Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release.
Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain.
The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive.
The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP.

## Action items

- Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive.
- MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required.
- Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only.
- Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.
- Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout.
- Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment.
- Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch.
- We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs.
