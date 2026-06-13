# Robust Counterfactual Paths under Distribution Shift

**Authors:** Adaeze Okonkwo, Kirill Petrov
**Year:** 2023
**Venue:** Advances in Neural Information Processing Systems 36 (NeurIPS 2023)
**arXiv:** 2306.99999
**Packet source:** added from memory

## Abstract (from packet)

Counterfactual explanations are known to be brittle under covariate shift and model updates: a recommended recourse path may cease to be valid when the underlying model is retrained on fresher data. We introduce *robust counterfactual paths*, a min-max formulation in which the generated counterfactual must remain valid under all classifiers in a bounded perturbation ball around the deployed model. Our approach builds on the FACE graph-traversal framework (Poyiadzi et al., 2020) but replaces the validity check with a robust certification step solved via convex relaxation. We prove that the resulting paths are valid for any classifier within a specified L∞ ball around the original and demonstrate robustness on three real-world tabular datasets, with only a modest cost increase (mean +18% L1 distance) relative to non-robust baselines.

## Notes
Robustness angle. Worth mentioning if we have space.
