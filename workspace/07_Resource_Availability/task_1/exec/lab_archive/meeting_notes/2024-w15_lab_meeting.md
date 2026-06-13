# Lab Meeting — 2024-04-19

## Standing items

- Compute partition status (Bao)
- IRB renewals (Priya)
- Slack-archive triage (Hari)
- Manuscript pipeline status (Yui)
- Federation client / Heron sync (Saanvi)
- Kestrel deployment health (Anika/Felix)
- Finch enrollment update (Devon/Talia)

## Updates

- Bao Nguyen: deprecated pipeline branches archived for v5
- Yui Tanaka: calibration plot bin boundaries updated, no surprises
- Marisol Holst: reviewer 3's distribution-shift question — drafting reply
- Erik Pohl: calibration plot bin boundaries updated, no surprises
- Erik Pohl: outcome-weighted IPCW patch in for review
- Renata Okonkwo: JBI revision continues, funding section still on Jay
- Talia Friedman: Heron round-4 model card under review
- Saanvi Desai: container rebuild done, no breaking changes
- Yui Tanaka: Finch wave-2 enrollment progressing
- Anika Sato: reviewer 3's distribution-shift question — drafting reply
- Yui Tanaka: clinical review batch underway
- Renata Okonkwo: JBI revision continues, funding section still on Jay

## Discussion notes

We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission.
The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required.
The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch.
Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year.

## Action items

- The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year.
- Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004.
- Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv.
- Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/.
- Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds.
- Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive.
- The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday.
- Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised.
