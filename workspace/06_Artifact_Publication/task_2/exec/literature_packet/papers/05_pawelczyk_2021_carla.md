# CARLA: A Python Library to Benchmark Algorithmic Recourse and Counterfactual Explanation Algorithms

**Authors:** Martin Pawelczyk, Sascha Bielawski, Johannes van den Heuvel, Tobias Richter, Gjergji Kasneci
**Year:** 2021
**Venue:** Advances in Neural Information Processing Systems 34 (NeurIPS 2021) Track on Datasets and Benchmarks
**arXiv:** 2108.00783
**Packet source:** collaborator email, 2026-05-12

## Abstract (from packet)

Counterfactual explanations and algorithmic recourse algorithms have proliferated, but a lack of consistent benchmarking has made cross-method comparison difficult: existing studies use inconsistent datasets, model classes, and evaluation metrics. We present CARLA (Counterfactual And Recourse LibrAry), an open-source Python framework that standardizes the comparison of counterfactual explanation methods on tabular data. CARLA provides (i) a unified API for invoking 11 published counterfactual generation methods (including Wachter-style optimization, DiCE, FACE, growing spheres, prototype-guided methods, and tree-based recourse algorithms), (ii) preconfigured benchmark datasets (Adult, COMPAS, GiveMeSomeCredit, HELOC) with standard preprocessing pipelines, and (iii) implementations of widely used evaluation metrics covering validity, proximity (L1/L2 in normalized space), sparsity, plausibility, redundancy, and run-time. We use CARLA to conduct what is, to our knowledge, the first large-scale empirical comparison of recourse algorithms under a unified protocol, and we report substantial sensitivity of method rankings to dataset and model class.

## Notes
Useful both as a benchmarking citation and because it implements all the baselines I'll want to compare to.
