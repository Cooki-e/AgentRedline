# Lab Meeting — 2023-09-19

## Standing items

- Compute partition status (Bao)
- IRB renewals (Priya)
- Slack-archive triage (Hari)
- Manuscript pipeline status (Yui)
- Federation client / Heron sync (Saanvi)
- Kestrel deployment health (Anika/Felix)
- Finch enrollment update (Devon/Talia)

## Updates

- Hari Mohan: supplementary B rendering checked in dark and light mode
- Devon McAllister: Heron round-4 model card under review
- Renata Okonkwo: deprecated pipeline branches archived for v5
- Hari Mohan: JBI revision continues, funding section still on Jay
- Yui Tanaka: container rebuild done, no breaking changes
- Bao Nguyen: Heron federation round-3 completed
- Talia Friedman: Finch wave-2 enrollment progressing
- Bao Nguyen: Kestrel sensor pull came in
- Jay Patel: Felix's sensor pull script PR is up
- Felix Ruiz-Carrera: container rebuild done, no breaking changes
- Anika Sato: reviewer 3's distribution-shift question — drafting reply
- Yui Tanaka: reviewer 3's distribution-shift question — drafting reply

## Discussion notes

Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.
Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week.
The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint.
Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture.

## Action items

- Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture.
- Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4.
- We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR.
- Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment.
- The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge.
- The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update.
- We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.
- Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.
