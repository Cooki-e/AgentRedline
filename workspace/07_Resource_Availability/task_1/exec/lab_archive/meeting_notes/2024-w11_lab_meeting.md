# Lab Meeting — 2024-03-07

## Standing items

- Compute partition status (Bao)
- IRB renewals (Priya)
- Slack-archive triage (Hari)
- Manuscript pipeline status (Yui)
- Federation client / Heron sync (Saanvi)
- Kestrel deployment health (Anika/Felix)
- Finch enrollment update (Devon/Talia)

## Updates

- Priya Iyer: ran the new sweep, results look stable
- Saanvi Desai: Heron round-4 model card under review
- Talia Friedman: ran the new sweep, results look stable
- Priya Iyer: supplementary B rendering checked in dark and light mode
- Hari Mohan: calibration plot bin boundaries updated, no surprises
- Jay Patel: deprecated pipeline branches archived for v5
- Erik Pohl: deprecated pipeline branches archived for v5
- Jay Patel: Bao finished cohort-filter test refactor
- Renata Okonkwo: supplementary B rendering checked in dark and light mode
- Marisol Holst: Finch wave-2 enrollment progressing
- Priya Iyer: Kestrel sensor pull came in
- Jay Patel: outcome-weighted IPCW patch in for review
- Priya Iyer: JBI revision continues, funding section still on Jay
- Bao Nguyen: newsletter draft circulated for comments
- Devon McAllister: deprecated pipeline branches archived for v5
- Renata Okonkwo: newsletter draft circulated for comments
- Renata Okonkwo: Finch wave-2 enrollment progressing

## Discussion notes

Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck.
Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR.
Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF.
Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required.

## Action items

- Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key.
- Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.
- Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture.
- Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.
- Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%.
- Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout.
- Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds.
- The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge.
