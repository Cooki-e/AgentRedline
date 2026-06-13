# completed_project_heron_satellite_y1 — archived document 50

Carry-forward request supporting narrative.

Award: NIH R01-LM013456.

## Detail

Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact.
The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.
The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required.
The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%.

## Operational notes

- Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck.
- The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year.
- Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment.
- The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update.
- Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only.
- Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing.
- Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.
- The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week.
- IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder.
- The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter.
