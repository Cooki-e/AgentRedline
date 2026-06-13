# Introduction

Counterfactual explanations [Wachter 2017; Mothilal 2020; Karimi 2020]
have become a workhorse for actionable recourse research. In clinical
settings, however, two issues recur: (a) constraints across feature
groups (immutable demographics, slow-moving comorbidities, mutable
physiologic measurements) are usually flattened into a single
feasibility cost, and (b) pathway feasibility — whether the suggested
change sequence is reachable from the current trajectory — is rarely
modeled explicitly. We address both.

[NOTE TO SELF — Yui, 2026-04-12: tighten this paragraph; Reviewer 1
wanted the recourse framing up top.]

The paper proceeds as follows. Section 2 surveys the relevant literature
across recourse, MACE-style optimization, model-agnostic methods,
feasibility / plausibility constraints, and benchmarking. Section 3
introduces our counterfactual pathway formulation. Section 4 reports
empirical results on MIMIC-IV and eICU. Section 5 reports a clinical
review with intensivists. Section 6 concludes.
