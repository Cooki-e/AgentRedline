# completed_project_heron_satellite_y1 — archived document 03

Annual NCE narrative justification.

Award: NIH R01-LM013456.

## Detail

The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance.
Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder.
Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain.
Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.

## Operational notes

- Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main.
- Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture.
- We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.
- Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features.
- Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog.
- Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending.
- IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder.
- Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP.
- Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF.
- Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.
