# Lab Meeting — 2024-11-16

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
- Marisol Holst: container rebuild done, no breaking changes
- Jay Patel: reviewer 3's distribution-shift question — drafting reply
- Erik Pohl: DUA addendum confirmed current
- Renata Okonkwo: Heron round-4 model card under review
- Felix Ruiz-Carrera: Kestrel sensor pull came in
- Bao Nguyen: Bao finished cohort-filter test refactor
- Marisol Holst: cohort filter passing validation
- Anika Sato: Kestrel sensor pull came in
- Bao Nguyen: supplementary B rendering checked in dark and light mode
- Erik Pohl: Finch wave-2 enrollment progressing
- Talia Friedman: Felix's sensor pull script PR is up
- Priya Iyer: Heron round-4 model card under review
- Saanvi Desai: supplementary B rendering checked in dark and light mode
- Hari Mohan: field-team dashboard refresh scheduled
- Anika Sato: ran the new sweep, results look stable
- Renata Okonkwo: ran the new sweep, results look stable

## Discussion notes

IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance.
Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment.
The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites.
Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/.

## Action items

- The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint.
- Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.
- The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter.
- We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR.
- Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%.
- Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only.
- Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive.
- MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required.
