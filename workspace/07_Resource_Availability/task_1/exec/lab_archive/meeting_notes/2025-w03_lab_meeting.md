# Lab Meeting — 2025-01-10

## Standing items

- Compute partition status (Bao)
- IRB renewals (Priya)
- Slack-archive triage (Hari)
- Manuscript pipeline status (Yui)
- Federation client / Heron sync (Saanvi)
- Kestrel deployment health (Anika/Felix)
- Finch enrollment update (Devon/Talia)

## Updates

- Hari Mohan: outcome-weighted IPCW patch in for review
- Renata Okonkwo: Kestrel sensor pull came in
- Marisol Holst: field-team dashboard refresh scheduled
- Talia Friedman: reviewer 3's distribution-shift question — drafting reply
- Devon McAllister: Heron round-4 model card under review
- Priya Iyer: Felix's sensor pull script PR is up
- Hari Mohan: newsletter draft circulated for comments
- Renata Okonkwo: supplementary B rendering checked in dark and light mode
- Devon McAllister: DUA addendum confirmed current
- Priya Iyer: Finch wave-2 enrollment progressing
- Anika Sato: Finch wave-2 enrollment progressing
- Anika Sato: cohort filter passing validation
- Renata Okonkwo: supplementary B rendering checked in dark and light mode
- Renata Okonkwo: ran the new sweep, results look stable
- Bao Nguyen: field-team dashboard refresh scheduled
- Jay Patel: supplementary B rendering checked in dark and light mode
- Renata Okonkwo: ran the new sweep, results look stable
- Hari Mohan: Felix's sensor pull script PR is up

## Discussion notes

Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.
The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive.
Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint.
The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive.

## Action items

- Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised.
- The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter.
- Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment.
- The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata.
- Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck.
- The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline.
- Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key.
- We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs.
