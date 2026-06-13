# Lab Meeting — 2024-07-01

## Standing items

- Compute partition status (Bao)
- IRB renewals (Priya)
- Slack-archive triage (Hari)
- Manuscript pipeline status (Yui)
- Federation client / Heron sync (Saanvi)
- Kestrel deployment health (Anika/Felix)
- Finch enrollment update (Devon/Talia)

## Updates

- Yui Tanaka: Finch wave-2 enrollment progressing
- Felix Ruiz-Carrera: clinical review batch underway
- Marisol Holst: container rebuild done, no breaking changes
- Saanvi Desai: reviewer 3's distribution-shift question — drafting reply
- Talia Friedman: supplementary B rendering checked in dark and light mode
- Jay Patel: Felix's sensor pull script PR is up
- Erik Pohl: deprecated pipeline branches archived for v5
- Hari Mohan: Heron federation round-3 completed
- Jay Patel: deprecated pipeline branches archived for v5
- Priya Iyer: Bao finished cohort-filter test refactor

## Discussion notes

The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment.
Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag.
Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy.
IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs.

## Action items

- Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised.
- Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts.
- The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline.
- MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required.
- Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds.
- Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only.
- Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture.
- Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff.
