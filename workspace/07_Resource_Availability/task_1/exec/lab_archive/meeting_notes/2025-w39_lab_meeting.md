# Lab Meeting — 2025-10-10

## Standing items

- Compute partition status (Bao)
- IRB renewals (Priya)
- Slack-archive triage (Hari)
- Manuscript pipeline status (Yui)
- Federation client / Heron sync (Saanvi)
- Kestrel deployment health (Anika/Felix)
- Finch enrollment update (Devon/Talia)

## Updates

- Marisol Holst: ran the new sweep, results look stable
- Devon McAllister: Finch wave-2 enrollment progressing
- Jay Patel: container rebuild done, no breaking changes
- Marisol Holst: ran the new sweep, results look stable
- Jay Patel: reviewer 3's distribution-shift question — drafting reply
- Hari Mohan: JBI revision continues, funding section still on Jay
- Erik Pohl: JBI revision continues, funding section still on Jay
- Felix Ruiz-Carrera: facility maintenance window next Tuesday
- Yui Tanaka: newsletter draft circulated for comments
- Anika Sato: ran the new sweep, results look stable
- Bao Nguyen: outcome-weighted IPCW patch in for review
- Saanvi Desai: calibration plot bin boundaries updated, no surprises
- Priya Iyer: facility maintenance window next Tuesday
- Felix Ruiz-Carrera: reviewer 3's distribution-shift question — drafting reply
- Yui Tanaka: cohort filter passing validation
- Erik Pohl: Felix's sensor pull script PR is up
- Anika Sato: deprecated pipeline branches archived for v5
- Anika Sato: supplementary B rendering checked in dark and light mode

## Discussion notes

Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing.
Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds.
Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR.
The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission.

## Action items

- Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF.
- Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck.
- Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key.
- The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week.
- Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.
- Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.
- Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation.
- Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only.
