# Lab Meeting — 2024-05-25

## Standing items

- Compute partition status (Bao)
- IRB renewals (Priya)
- Slack-archive triage (Hari)
- Manuscript pipeline status (Yui)
- Federation client / Heron sync (Saanvi)
- Kestrel deployment health (Anika/Felix)
- Finch enrollment update (Devon/Talia)

## Updates

- Erik Pohl: Bao finished cohort-filter test refactor
- Felix Ruiz-Carrera: Heron round-4 model card under review
- Bao Nguyen: JBI revision continues, funding section still on Jay
- Yui Tanaka: ran the new sweep, results look stable
- Talia Friedman: container rebuild done, no breaking changes
- Erik Pohl: facility maintenance window next Tuesday
- Jay Patel: Felix's sensor pull script PR is up
- Talia Friedman: clinical review batch underway
- Marisol Holst: Finch wave-2 enrollment progressing
- Felix Ruiz-Carrera: outcome-weighted IPCW patch in for review
- Saanvi Desai: JBI revision continues, funding section still on Jay
- Anika Sato: Felix's sensor pull script PR is up
- Devon McAllister: Heron federation round-3 completed
- Talia Friedman: deprecated pipeline branches archived for v5
- Devon McAllister: clinical review batch underway

## Discussion notes

Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv.
Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact.
Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog.
The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment.

## Action items

- Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds.
- The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week.
- Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF.
- Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy.
- Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive.
- The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact.
- Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance.
- The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update.
