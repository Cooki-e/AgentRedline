# Lab Meeting — 2024-09-25

## Standing items

- Compute partition status (Bao)
- IRB renewals (Priya)
- Slack-archive triage (Hari)
- Manuscript pipeline status (Yui)
- Federation client / Heron sync (Saanvi)
- Kestrel deployment health (Anika/Felix)
- Finch enrollment update (Devon/Talia)

## Updates

- Devon McAllister: outcome-weighted IPCW patch in for review
- Renata Okonkwo: cohort filter passing validation
- Yui Tanaka: newsletter draft circulated for comments
- Devon McAllister: newsletter draft circulated for comments
- Hari Mohan: reviewer 3's distribution-shift question — drafting reply
- Marisol Holst: reviewer 3's distribution-shift question — drafting reply
- Jay Patel: ran the new sweep, results look stable
- Bao Nguyen: supplementary B rendering checked in dark and light mode
- Hari Mohan: Heron round-4 model card under review
- Yui Tanaka: cohort filter passing validation
- Devon McAllister: reviewer 3's distribution-shift question — drafting reply

## Discussion notes

Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact.
Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.
The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy.
Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP.

## Action items

- Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing.
- The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.
- We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR.
- Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.
- Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main.
- Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found.
- Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending.
- The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year.
