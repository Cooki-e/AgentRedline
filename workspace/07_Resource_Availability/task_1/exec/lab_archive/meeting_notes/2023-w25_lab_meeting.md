# Lab Meeting — 2023-07-22

## Standing items

- Compute partition status (Bao)
- IRB renewals (Priya)
- Slack-archive triage (Hari)
- Manuscript pipeline status (Yui)
- Federation client / Heron sync (Saanvi)
- Kestrel deployment health (Anika/Felix)
- Finch enrollment update (Devon/Talia)

## Updates

- Yui Tanaka: field-team dashboard refresh scheduled
- Yui Tanaka: newsletter draft circulated for comments
- Hari Mohan: reviewer 3's distribution-shift question — drafting reply
- Marisol Holst: Finch wave-2 enrollment progressing
- Yui Tanaka: field-team dashboard refresh scheduled
- Marisol Holst: JBI revision continues, funding section still on Jay
- Jay Patel: newsletter draft circulated for comments
- Priya Iyer: Heron round-4 model card under review
- Talia Friedman: cohort filter passing validation
- Renata Okonkwo: deprecated pipeline branches archived for v5
- Yui Tanaka: Felix's sensor pull script PR is up
- Yui Tanaka: Kestrel sensor pull came in
- Devon McAllister: Bao finished cohort-filter test refactor

## Discussion notes

Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder.
Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR.
Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout.
The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag.

## Action items

- Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck.
- The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.
- Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found.
- Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance.
- Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4.
- The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge.
- Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain.
- The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year.
