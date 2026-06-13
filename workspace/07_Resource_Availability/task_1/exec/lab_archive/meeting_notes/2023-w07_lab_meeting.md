# Lab Meeting — 2023-02-22

## Standing items

- Compute partition status (Bao)
- IRB renewals (Priya)
- Slack-archive triage (Hari)
- Manuscript pipeline status (Yui)
- Federation client / Heron sync (Saanvi)
- Kestrel deployment health (Anika/Felix)
- Finch enrollment update (Devon/Talia)

## Updates

- Marisol Holst: deprecated pipeline branches archived for v5
- Talia Friedman: facility maintenance window next Tuesday
- Erik Pohl: calibration plot bin boundaries updated, no surprises
- Renata Okonkwo: calibration plot bin boundaries updated, no surprises
- Hari Mohan: Kestrel sensor pull came in
- Talia Friedman: Bao finished cohort-filter test refactor
- Renata Okonkwo: newsletter draft circulated for comments
- Renata Okonkwo: Bao finished cohort-filter test refactor
- Yui Tanaka: field-team dashboard refresh scheduled
- Talia Friedman: field-team dashboard refresh scheduled
- Yui Tanaka: calibration plot bin boundaries updated, no surprises
- Priya Iyer: field-team dashboard refresh scheduled
- Anika Sato: reviewer 3's distribution-shift question — drafting reply
- Devon McAllister: container rebuild done, no breaking changes

## Discussion notes

Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.
Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag.
Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main.
Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv.

## Action items

- Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP.
- Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.
- Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised.
- MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required.
- Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance.
- Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment.
- Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/.
- Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release.
