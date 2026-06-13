# completed_project_kestrel_y2 — archived document 28

Travel reimbursement form (redacted).

Award: NSF IIS-2031234.

## Detail

The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year.
Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission.
The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter.
Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week.

## Operational notes

- Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment.
- Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag.
- MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required.
- Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key.
- We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.
- The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.
- Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004.
- The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter.
- Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites.
- The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year.
