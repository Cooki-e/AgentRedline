# Lab Meeting — 2025-11-16

## Standing items

- Compute partition status (Bao)
- IRB renewals (Priya)
- Slack-archive triage (Hari)
- Manuscript pipeline status (Yui)
- Federation client / Heron sync (Saanvi)
- Kestrel deployment health (Anika/Felix)
- Finch enrollment update (Devon/Talia)

## Updates

- Felix Ruiz-Carrera: Kestrel sensor pull came in
- Felix Ruiz-Carrera: Heron federation round-3 completed
- Yui Tanaka: JBI revision continues, funding section still on Jay
- Yui Tanaka: DUA addendum confirmed current
- Talia Friedman: reviewer 3's distribution-shift question — drafting reply
- Jay Patel: supplementary B rendering checked in dark and light mode
- Yui Tanaka: supplementary B rendering checked in dark and light mode
- Devon McAllister: supplementary B rendering checked in dark and light mode
- Felix Ruiz-Carrera: newsletter draft circulated for comments
- Bao Nguyen: newsletter draft circulated for comments
- Bao Nguyen: Felix's sensor pull script PR is up
- Renata Okonkwo: clinical review batch underway
- Yui Tanaka: cohort filter passing validation
- Saanvi Desai: field-team dashboard refresh scheduled

## Discussion notes

Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.
We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter.
MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF.
MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds.

## Action items

- The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday.
- Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged.
- Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release.
- Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation.
- Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts.
- Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture.
- We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs.
- Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy.
