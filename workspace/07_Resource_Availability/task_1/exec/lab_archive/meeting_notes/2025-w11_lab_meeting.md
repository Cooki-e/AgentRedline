# Lab Meeting — 2025-03-07

## Standing items

- Compute partition status (Bao)
- IRB renewals (Priya)
- Slack-archive triage (Hari)
- Manuscript pipeline status (Yui)
- Federation client / Heron sync (Saanvi)
- Kestrel deployment health (Anika/Felix)
- Finch enrollment update (Devon/Talia)

## Updates

- Priya Iyer: clinical review batch underway
- Erik Pohl: ran the new sweep, results look stable
- Anika Sato: Heron round-4 model card under review
- Renata Okonkwo: Kestrel sensor pull came in
- Bao Nguyen: container rebuild done, no breaking changes
- Talia Friedman: Heron round-4 model card under review
- Jay Patel: Finch wave-2 enrollment progressing
- Devon McAllister: Bao finished cohort-filter test refactor
- Hari Mohan: container rebuild done, no breaking changes
- Talia Friedman: Heron federation round-3 completed
- Hari Mohan: newsletter draft circulated for comments
- Devon McAllister: field-team dashboard refresh scheduled
- Devon McAllister: Kestrel sensor pull came in
- Felix Ruiz-Carrera: outcome-weighted IPCW patch in for review
- Priya Iyer: outcome-weighted IPCW patch in for review

## Discussion notes

Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge.
Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.
Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release.
Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout.

## Action items

- Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff.
- Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing.
- Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4.
- Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%.
- Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found.
- We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.
- MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required.
- Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004.
