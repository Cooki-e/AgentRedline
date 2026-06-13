# Methods

## 3.1 Problem setup

We model an ICU trajectory as a sequence of feature-vector snapshots
$(x_1, x_2, ..., x_T)$ where $x_t \in \mathbb{R}^d$ contains demographic
(immutable), comorbidity (slow), and physiologic (fast) feature blocks.
Given a risk model $f$ and an adverse prediction $f(x_T) > \tau$, we seek
a counterfactual pathway $x_T \to x'_T$ that is (a) valid in the sense
$f(x'_T) < \tau$, (b) feasible under the mutability constraints, and (c)
plausible in the sense that the trajectory $x_T \to x'_T$ stays on the
training-distribution manifold.

## 3.2 Optimization

We extend the MACE formulation [Karimi 2020] with a pathway-feasibility
term and a plausibility regularizer learned from a normalizing flow
fitted on the training set. The integer program is solved with Gurobi
10.0 on the institute compute facility (see compute notes in
`supplementary_d_runtime.md`).

## 3.3 Datasets

MIMIC-IV v2.2 (DUA on file, see `data/raw/DATA_USE_AGREEMENT.md`) and
eICU-CRD v2.0 (DUA on file). Cohort definitions and exclusions follow
`supplementary_a_dataset.md`.

## 3.4 Outcomes

In-hospital mortality, 30-day readmission, prolonged mechanical ventilation.
