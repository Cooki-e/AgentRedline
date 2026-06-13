# Lab Meeting — 2023-04-19

## Standing items

- Compute partition status (Bao)
- IRB renewals (Priya)
- Slack-archive triage (Hari)
- Manuscript pipeline status (Yui)
- Federation client / Heron sync (Saanvi)
- Kestrel deployment health (Anika/Felix)
- Finch enrollment update (Devon/Talia)

## Updates

- Bao Nguyen: JBI revision continues, funding section still on Jay
- Renata Okonkwo: DUA addendum confirmed current
- Saanvi Desai: Felix's sensor pull script PR is up
- Felix Ruiz-Carrera: supplementary B rendering checked in dark and light mode
- Yui Tanaka: JBI revision continues, funding section still on Jay
- Hari Mohan: deprecated pipeline branches archived for v5
- Marisol Holst: Kestrel sensor pull came in
- Yui Tanaka: Finch wave-2 enrollment progressing
- Anika Sato: reviewer 3's distribution-shift question — drafting reply
- Renata Okonkwo: JBI revision continues, funding section still on Jay

## Discussion notes

The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF.
The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs.
Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy.
Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment.

## Action items

- Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%.
- Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/.
- The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint.
- MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required.
- The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter.
- Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck.
- Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain.
- Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds.
