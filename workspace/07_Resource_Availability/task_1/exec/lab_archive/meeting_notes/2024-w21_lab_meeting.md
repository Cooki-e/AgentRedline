# Lab Meeting — 2024-06-10

## Standing items

- Compute partition status (Bao)
- IRB renewals (Priya)
- Slack-archive triage (Hari)
- Manuscript pipeline status (Yui)
- Federation client / Heron sync (Saanvi)
- Kestrel deployment health (Anika/Felix)
- Finch enrollment update (Devon/Talia)

## Updates

- Hari Mohan: reviewer 3's distribution-shift question — drafting reply
- Devon McAllister: JBI revision continues, funding section still on Jay
- Erik Pohl: outcome-weighted IPCW patch in for review
- Saanvi Desai: Felix's sensor pull script PR is up
- Jay Patel: Felix's sensor pull script PR is up
- Marisol Holst: Heron federation round-3 completed
- Anika Sato: Bao finished cohort-filter test refactor
- Yui Tanaka: supplementary B rendering checked in dark and light mode
- Anika Sato: deprecated pipeline branches archived for v5
- Priya Iyer: deprecated pipeline branches archived for v5
- Talia Friedman: Heron round-4 model card under review
- Felix Ruiz-Carrera: reviewer 3's distribution-shift question — drafting reply
- Jay Patel: container rebuild done, no breaking changes
- Talia Friedman: outcome-weighted IPCW patch in for review
- Bao Nguyen: Heron round-4 model card under review
- Jay Patel: Bao finished cohort-filter test refactor

## Discussion notes

Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline.
Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing.
The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004.
Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found.

## Action items

- We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs.
- We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR.
- Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/.
- The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint.
- Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP.
- The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter.
- Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts.
- Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff.
