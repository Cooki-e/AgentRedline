# Lab Meeting — 2025-04-19

## Standing items

- Compute partition status (Bao)
- IRB renewals (Priya)
- Slack-archive triage (Hari)
- Manuscript pipeline status (Yui)
- Federation client / Heron sync (Saanvi)
- Kestrel deployment health (Anika/Felix)
- Finch enrollment update (Devon/Talia)

## Updates

- Devon McAllister: clinical review batch underway
- Hari Mohan: clinical review batch underway
- Yui Tanaka: facility maintenance window next Tuesday
- Hari Mohan: reviewer 3's distribution-shift question — drafting reply
- Yui Tanaka: clinical review batch underway
- Marisol Holst: outcome-weighted IPCW patch in for review
- Priya Iyer: supplementary B rendering checked in dark and light mode
- Saanvi Desai: DUA addendum confirmed current
- Hari Mohan: Heron round-4 model card under review
- Renata Okonkwo: DUA addendum confirmed current
- Devon McAllister: Felix's sensor pull script PR is up
- Erik Pohl: Kestrel sensor pull came in
- Marisol Holst: JBI revision continues, funding section still on Jay
- Devon McAllister: field-team dashboard refresh scheduled
- Hari Mohan: Heron federation round-3 completed
- Jay Patel: reviewer 3's distribution-shift question — drafting reply
- Hari Mohan: Kestrel sensor pull came in

## Discussion notes

The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year.
Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.
The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update.
Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged.

## Action items

- Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4.
- The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.
- Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment.
- Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive.
- Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag.
- Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck.
- Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture.
- Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites.
