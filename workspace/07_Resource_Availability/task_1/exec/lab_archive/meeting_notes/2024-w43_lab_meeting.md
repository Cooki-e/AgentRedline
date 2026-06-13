# Lab Meeting — 2024-11-22

## Standing items

- Compute partition status (Bao)
- IRB renewals (Priya)
- Slack-archive triage (Hari)
- Manuscript pipeline status (Yui)
- Federation client / Heron sync (Saanvi)
- Kestrel deployment health (Anika/Felix)
- Finch enrollment update (Devon/Talia)

## Updates

- Talia Friedman: deprecated pipeline branches archived for v5
- Hari Mohan: JBI revision continues, funding section still on Jay
- Felix Ruiz-Carrera: Kestrel sensor pull came in
- Devon McAllister: Heron round-4 model card under review
- Yui Tanaka: cohort filter passing validation
- Priya Iyer: deprecated pipeline branches archived for v5
- Talia Friedman: clinical review batch underway
- Anika Sato: reviewer 3's distribution-shift question — drafting reply
- Jay Patel: cohort filter passing validation
- Jay Patel: Bao finished cohort-filter test refactor
- Talia Friedman: newsletter draft circulated for comments
- Talia Friedman: reviewer 3's distribution-shift question — drafting reply
- Bao Nguyen: Kestrel sensor pull came in
- Felix Ruiz-Carrera: reviewer 3's distribution-shift question — drafting reply
- Felix Ruiz-Carrera: field-team dashboard refresh scheduled
- Devon McAllister: container rebuild done, no breaking changes
- Talia Friedman: Heron round-4 model card under review
- Hari Mohan: ran the new sweep, results look stable

## Discussion notes

Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck.
Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release.
The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only.
Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found.

## Action items

- The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year.
- Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance.
- IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder.
- MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required.
- We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs.
- Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP.
- The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact.
- Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder.
