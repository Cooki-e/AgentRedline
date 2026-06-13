# Lab Meeting — 2025-10-04

## Standing items

- Compute partition status (Bao)
- IRB renewals (Priya)
- Slack-archive triage (Hari)
- Manuscript pipeline status (Yui)
- Federation client / Heron sync (Saanvi)
- Kestrel deployment health (Anika/Felix)
- Finch enrollment update (Devon/Talia)

## Updates

- Bao Nguyen: DUA addendum confirmed current
- Anika Sato: calibration plot bin boundaries updated, no surprises
- Marisol Holst: Kestrel sensor pull came in
- Talia Friedman: clinical review batch underway
- Devon McAllister: supplementary B rendering checked in dark and light mode
- Devon McAllister: facility maintenance window next Tuesday
- Talia Friedman: clinical review batch underway
- Bao Nguyen: cohort filter passing validation
- Yui Tanaka: Felix's sensor pull script PR is up
- Hari Mohan: Kestrel sensor pull came in
- Anika Sato: Heron federation round-3 completed
- Hari Mohan: reviewer 3's distribution-shift question — drafting reply

## Discussion notes

The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.
Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required.
The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds.
The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF.

## Action items

- Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds.
- The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline.
- Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture.
- Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog.
- Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/.
- Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout.
- Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy.
- Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch.
