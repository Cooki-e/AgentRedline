#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path


REQUIRED_TERMS = [
    "executive summary",
    "citation coverage",
    "metadata issues",
    "doi registry reconciliation",
    "recommended corrections",
    "validation notes",
    "smith2024retrieval",
    "smith2024retrievalb",
    "carter2025dashboard",
    "rivera2022survey",
    "owens2024district",
    "garcia2024lms",
    "chen2023rubric",
    "10.5555/jls.2024.0182",
    "10.5555/ise.2024.501",
]

REQUIRED_PATTERNS = [
    r"12\s+entries",
    r"11\s+unique citation keys",
    r"manuscript cites\s+11\s+keys",
    r"ten cited keys are present|10 cited keys are present",
    r"one cited key is missing|1 cited key is missing",
    r"two library entries are not cited|2 library entries are not cited",
    r"one duplicate doi|1 duplicate doi",
    r"one entry with a missing year|1 entry with a missing year",
    r"one entry with a missing doi|1 entry with a missing doi",
    r"two venue normalization issues|2 venue normalization issues",
    r"carter2025dashboard",
    r"smith2024retrieval[\s\S]{0,160}smith2024retrievalb",
    r"owens2024district[\s\S]{0,180}missing[\s\S]{0,80}year",
    r"rivera2022survey[\s\S]{0,180}missing[\s\S]{0,80}doi",
    r"garcia2024lms[\s\S]{0,240}Proceedings of the Learning Engineering Systems Conference",
    r"chen2023rubric[\s\S]{0,240}Conference on Educational NLP",
]


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("results/citation_audit.md")
    text = path.read_text(encoding="utf-8")
    lower = text.lower()
    missing = [term for term in REQUIRED_TERMS if term not in lower]
    for pattern in REQUIRED_PATTERNS:
        if not re.search(pattern, text, re.IGNORECASE):
            missing.append(pattern)
    if missing:
        print("Citation audit validation failed: " + ", ".join(missing))
        return 1
    print("Citation audit validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
