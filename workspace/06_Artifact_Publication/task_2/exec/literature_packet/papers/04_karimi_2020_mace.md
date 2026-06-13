# Model-Agnostic Counterfactual Explanations for Consequential Decisions

**Authors:** Amir-Hossein Karimi, Gilles Barthe, Borja Balle, Isabel Valera
**Year:** 2020
**Venue:** Proceedings of the 23rd International Conference on Artificial Intelligence and Statistics (AISTATS 2020), PMLR 108:895–905
**arXiv:** 1905.11190
**Packet source:** reference list of Pawelczyk 2021

## Abstract (from packet)

Recent work has discussed the limitations of counterfactual explanations to recommend actions that an individual could take to overturn an unfavorable decision (algorithmic recourse). We present a model-agnostic method, MACE, that generates nearest counterfactual explanations for any classifier representable as a set of logical formulas, including decision trees, random forests, and multi-layer perceptrons. MACE reduces counterfactual search to a sequence of satisfiability (SAT) problems and admits a rich language of user-specified plausibility and actionability constraints — including categorical immutability, monotone-only changes, and pairwise feature dependencies — without relying on the differentiability of the underlying model. We prove correctness and present an efficient implementation using off-the-shelf SMT solvers. Experiments on standard fairness benchmarks (Adult, German Credit, COMPAS) show that MACE finds counterfactuals that respect plausibility constraints at competitive distances compared to gradient-based and search-based baselines.

## Notes
Important as a foil for gradient-based methods like DiCE.
