# FACE: Feasible and Actionable Counterfactual Explanations

**Authors:** Rafael Poyiadzi, Kacper Sokol, Raul Santos-Rodriguez, Tijl De Bie, Peter Flach
**Year:** 2020
**Venue:** Proceedings of the 2020 AAAI/ACM Conference on AI, Ethics, and Society (AIES 2020), pp. 344–350
**DOI:** 10.1145/3375627.3375850
**arXiv:** 1909.09369
**Packet source:** collaborator email, 2026-05-12

## Abstract (from packet)

Counterfactual explanations of model decisions are often produced as the result of an unconstrained optimization, which can return implausible or unreachable points that lie far from the data manifold. We propose FACE (Feasible and Actionable Counterfactual Explanations), a method that produces counterfactuals along *feasible paths* through the training data. FACE constructs a weighted graph over the training set where edge weights reflect density along the line segment between two points (estimated using a kernel density estimator), and recovers counterfactual paths by running shortest-path search from the query point to the nearest point of the target class. The resulting counterfactuals are not only close in distance but reachable via a sequence of plausible intermediate points, addressing a known failure mode of optimization-based counterfactuals that hop across low-density regions. We demonstrate FACE on UCI datasets and discuss its application to algorithmic recourse, where path feasibility maps naturally to a sequence of incremental actions an individual could take.

## Notes
Plausibility / feasibility angle. Key citation for the data-manifold thread.
