# Lab Meeting — 2023-08-13

## Standing items

- Compute partition status (Bao)
- IRB renewals (Priya)
- Slack-archive triage (Hari)
- Manuscript pipeline status (Yui)
- Federation client / Heron sync (Saanvi)
- Kestrel deployment health (Anika/Felix)
- Finch enrollment update (Devon/Talia)

## Updates

- Erik Pohl: field-team dashboard refresh scheduled
- Hari Mohan: deprecated pipeline branches archived for v5
- Jay Patel: DUA addendum confirmed current
- Hari Mohan: facility maintenance window next Tuesday
- Anika Sato: outcome-weighted IPCW patch in for review
- Bao Nguyen: Finch wave-2 enrollment progressing
- Renata Okonkwo: supplementary B rendering checked in dark and light mode
- Felix Ruiz-Carrera: field-team dashboard refresh scheduled
- Jay Patel: newsletter draft circulated for comments
- Felix Ruiz-Carrera: JBI revision continues, funding section still on Jay
- Erik Pohl: ran the new sweep, results look stable
- Talia Friedman: DUA addendum confirmed current
- Felix Ruiz-Carrera: deprecated pipeline branches archived for v5
- Saanvi Desai: field-team dashboard refresh scheduled
- Talia Friedman: cohort filter passing validation
- Jay Patel: facility maintenance window next Tuesday
- Renata Okonkwo: ran the new sweep, results look stable

## Discussion notes

Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline.
Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy.
We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%.
Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004.

## Action items

- Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP.
- Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds.
- IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder.
- The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week.
- MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required.
- We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR.
- Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch.
- The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact.
