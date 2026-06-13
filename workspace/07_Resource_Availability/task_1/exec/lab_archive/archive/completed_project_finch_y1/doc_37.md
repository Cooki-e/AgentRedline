# completed_project_finch_y1 — archived document 37

Subaward modification memo.

Award: NIH R01-AG056789.

## Detail

Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites.
Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required.
Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge.
Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain.

## Operational notes

- The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter.
- The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact.
- Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP.
- Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only.
- Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release.
- We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR.
- Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004.
- Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission.
- The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year.
- Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features.
