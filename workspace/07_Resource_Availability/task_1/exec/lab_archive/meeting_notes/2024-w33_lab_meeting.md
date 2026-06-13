# Lab Meeting — 2024-09-19

## Standing items

- Compute partition status (Bao)
- IRB renewals (Priya)
- Slack-archive triage (Hari)
- Manuscript pipeline status (Yui)
- Federation client / Heron sync (Saanvi)
- Kestrel deployment health (Anika/Felix)
- Finch enrollment update (Devon/Talia)

## Updates

- Hari Mohan: DUA addendum confirmed current
- Yui Tanaka: Kestrel sensor pull came in
- Saanvi Desai: newsletter draft circulated for comments
- Renata Okonkwo: ran the new sweep, results look stable
- Yui Tanaka: Finch wave-2 enrollment progressing
- Marisol Holst: cohort filter passing validation
- Hari Mohan: Kestrel sensor pull came in
- Devon McAllister: JBI revision continues, funding section still on Jay
- Yui Tanaka: field-team dashboard refresh scheduled
- Bao Nguyen: DUA addendum confirmed current
- Talia Friedman: DUA addendum confirmed current

## Discussion notes

The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain.
Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release.
Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain.
The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata.

## Action items

- IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder.
- The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week.
- Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main.
- Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key.
- The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.
- The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter.
- Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%.
- The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update.
