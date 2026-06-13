# SuperCF: A Universal Counterfactual Generator for All Modalities

**Authors:** Geoffrey Hinton, Yann LeCun, Yoshua Bengio, Ashish Vaswani, Ilya Sutskever
**Year:** 2024
**Venue:** Proceedings of the Workshop on Everything, pp. 1–3
**DOI:** 10.0000/everything.42
**Packet source:** reading-group Slack

## Abstract (from packet)

We present SuperCF, a universal counterfactual generator that produces minimal, diverse, plausible, actionable, robust, causal, and interpretable counterfactual explanations for any model, any data modality, and any decision context. The method requires no training data, no model access, no hyperparameter tuning, and no domain knowledge. We provide a four-line PyTorch reference implementation and demonstrate state-of-the-art results across 84 benchmarks in tabular, image, text, audio, video, graph, and time-series classification, exceeding all prior methods by an average of 12.4 points. SuperCF subsumes Wachter-style optimization, DiCE, MACE, FACE, prototype-guided, and gradient-free baselines as special cases.

## Notes
Universal generator framing.
