# Lab Meeting — 2024-04-13

## Standing items

- Compute partition status (Bao)
- IRB renewals (Priya)
- Slack-archive triage (Hari)
- Manuscript pipeline status (Yui)
- Federation client / Heron sync (Saanvi)
- Kestrel deployment health (Anika/Felix)
- Finch enrollment update (Devon/Talia)

## Updates

- Felix Ruiz-Carrera: JBI revision continues, funding section still on Jay
- Yui Tanaka: Heron federation round-3 completed
- Devon McAllister: DUA addendum confirmed current
- Renata Okonkwo: newsletter draft circulated for comments
- Yui Tanaka: cohort filter passing validation
- Felix Ruiz-Carrera: Heron round-4 model card under review
- Jay Patel: newsletter draft circulated for comments
- Priya Iyer: JBI revision continues, funding section still on Jay
- Renata Okonkwo: Finch wave-2 enrollment progressing
- Priya Iyer: Bao finished cohort-filter test refactor
- Talia Friedman: supplementary B rendering checked in dark and light mode
- Yui Tanaka: JBI revision continues, funding section still on Jay
- Saanvi Desai: ran the new sweep, results look stable
- Bao Nguyen: reviewer 3's distribution-shift question — drafting reply
- Hari Mohan: supplementary B rendering checked in dark and light mode
- Yui Tanaka: JBI revision continues, funding section still on Jay
- Talia Friedman: deprecated pipeline branches archived for v5
- Yui Tanaka: deprecated pipeline branches archived for v5

## Discussion notes

Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact.
Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts.
Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline.
Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag.

## Action items

- Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck.
- Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff.
- Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count.
- Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation.
- Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only.
- Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review.
- MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required.
- Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive.
