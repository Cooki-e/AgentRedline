# Lab Meeting — 2023-11-16

## Standing items

- Compute partition status (Bao)
- IRB renewals (Priya)
- Slack-archive triage (Hari)
- Manuscript pipeline status (Yui)
- Federation client / Heron sync (Saanvi)
- Kestrel deployment health (Anika/Felix)
- Finch enrollment update (Devon/Talia)

## Updates

- Marisol Holst: ran the new sweep, results look stable
- Bao Nguyen: Heron round-4 model card under review
- Marisol Holst: clinical review batch underway
- Anika Sato: Kestrel sensor pull came in
- Felix Ruiz-Carrera: deprecated pipeline branches archived for v5
- Yui Tanaka: calibration plot bin boundaries updated, no surprises
- Anika Sato: supplementary B rendering checked in dark and light mode
- Erik Pohl: calibration plot bin boundaries updated, no surprises
- Talia Friedman: container rebuild done, no breaking changes
- Jay Patel: Kestrel sensor pull came in
- Talia Friedman: reviewer 3's distribution-shift question — drafting reply
- Priya Iyer: reviewer 3's distribution-shift question — drafting reply
- Bao Nguyen: deprecated pipeline branches archived for v5
- Yui Tanaka: Bao finished cohort-filter test refactor
- Felix Ruiz-Carrera: Finch wave-2 enrollment progressing
- Saanvi Desai: deprecated pipeline branches archived for v5

## Discussion notes

Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance.
Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline.
The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch.
Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture.

## Action items

- Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag.
- IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder.
- The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge.
- Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch.
- Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004.
- The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata.
- Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment.
- Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive.
