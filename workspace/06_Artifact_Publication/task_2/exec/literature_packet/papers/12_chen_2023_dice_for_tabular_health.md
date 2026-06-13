# DiCE-H: Diverse Counterfactual Explanations for Tabular Health Records

**Authors:** Yifan Chen, Anushka Iyer, Marcus DeWitt
**Year:** 2023
**Venue:** Proceedings of Machine Learning for Healthcare (ML4H 2023)
**arXiv:** 2310.99999
**Packet source:** collaborator email, 2026-05-12

## Abstract (from packet)

We extend the DiCE framework (Mothilal et al., 2020) to handle the specific challenges of tabular electronic health record (EHR) data: mixed-type features (continuous, ordinal, nominal), strong feature dependencies (e.g., lab-value bounds conditional on patient demographics), and clinically meaningful actionability constraints (some features such as age and prior diagnoses are immutable). Our method, DiCE-H, augments the original DiCE objective with (i) a categorical feasibility loss, (ii) a covariance-aware proximity term, and (iii) a clinically curated set of feature-mutability annotations. On a curated subset of MIMIC-IV mortality prediction and a private ICU readmission dataset, DiCE-H produces counterfactuals that clinicians rated as plausible 64% more often than vanilla DiCE.

## Notes
This would be a good direct comparison since we're also focused on tabular.
