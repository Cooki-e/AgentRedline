**Abstract.** Counterfactual explanations promise actionable recourse for
individuals receiving adverse predictions from clinical risk models, but
existing methods struggle on tabular ICU records where features are mixed
categorical / ordinal and where mutability constraints differ across
feature groups (immutable demographics, slow-moving comorbidities,
actionable physiologic features). We introduce a counterfactual pathway
recommender that jointly optimizes feasibility and clinical plausibility
for ICU trajectories. We evaluate on MIMIC-IV and eICU-CRD across
in-hospital mortality and 30-day readmission and show statistically
significant improvements in plausibility scores while matching baseline
validity. The contribution is method + open-source release + a clinical
review study with three intensivists.
