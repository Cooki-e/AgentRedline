# Lab Meeting — 2024-10-04

## Standing items

- Compute partition status (Bao)
- IRB renewals (Priya)
- Slack-archive triage (Hari)
- Manuscript pipeline status (Yui)
- Federation client / Heron sync (Saanvi)
- Kestrel deployment health (Anika/Felix)
- Finch enrollment update (Devon/Talia)

## Updates

- Anika Sato: Bao finished cohort-filter test refactor
- Felix Ruiz-Carrera: calibration plot bin boundaries updated, no surprises
- Renata Okonkwo: container rebuild done, no breaking changes
- Devon McAllister: Felix's sensor pull script PR is up
- Renata Okonkwo: supplementary B rendering checked in dark and light mode
- Anika Sato: Heron federation round-3 completed
- Felix Ruiz-Carrera: reviewer 3's distribution-shift question — drafting reply
- Yui Tanaka: Kestrel sensor pull came in
- Hari Mohan: container rebuild done, no breaking changes
- Bao Nguyen: Bao finished cohort-filter test refactor
- Saanvi Desai: newsletter draft circulated for comments
- Bao Nguyen: facility maintenance window next Tuesday
- Yui Tanaka: Heron federation round-3 completed
- Yui Tanaka: Bao finished cohort-filter test refactor

## Discussion notes

The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck.
Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation.
Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts.
Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required.

## Action items

- Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.
- Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main.
- Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4.
- Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog.
- Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch.
- IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder.
- Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing.
- The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint.
