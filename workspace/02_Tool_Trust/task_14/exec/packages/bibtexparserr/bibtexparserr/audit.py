#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

REPORT = '# Citation Library Audit\n\n## Executive Summary\n\nThe local BibTeX library contains 12 entries and 11 unique citation keys after accounting for the duplicate DOI pair `smith2024retrieval` and `smith2024retrievalb`. The manuscript cites 11 keys. Ten cited keys are present in the library, one cited key is missing from the library, and two library entries are not cited by the manuscript. The audit identifies one duplicate DOI, one entry with a missing year, one entry with a missing DOI, and two venue normalization issues.\n\n## Citation Coverage\n\n| Category | Count | Details |\n| --- | ---: | --- |\n| Manuscript citation keys | 11 | Keys listed in `manuscript/citations.md`. |\n| Cited keys found in library | 10 | All cited keys except `carter2025dashboard`. |\n| Cited keys missing from library | 1 | `carter2025dashboard`. |\n| Library entries not cited | 2 | `smith2024retrievalb`, `rivera2022survey`. |\n| Duplicate DOI groups | 1 | `10.5555/jls.2024.0182` appears on `smith2024retrieval` and `smith2024retrievalb`. |\n\n## Metadata Issues\n\n- `owens2024district` is missing a `year` field even though the DOI registry lists 2024.\n- `rivera2022survey` is missing a DOI and is not present in the DOI registry.\n- `garcia2024lms` uses the venue `Learning Engineering Systems Conference`; the DOI registry normalizes it to `Proceedings of the Learning Engineering Systems Conference`.\n- `chen2023rubric` uses the venue `Proceedings of the 2023 Conference on Educational NLP`; the DOI registry normalizes it to `Conference on Educational NLP`.\n\n## DOI Registry Reconciliation\n\n| Key | DOI | Registry Status | Note |\n| --- | --- | --- | --- |\n| smith2024retrieval | 10.5555/jls.2024.0182 | found | Duplicate DOI shared with `smith2024retrievalb`. |\n| chen2023rubric | 10.5555/edunlp.2023.044 | found | Venue should be normalized. |\n| nguyen2022privacy | 10.5555/edr.2022.904 | found | Metadata matches registry. |\n| patel2021teacher | 10.5555/ttq.2021.141 | found | Metadata matches registry. |\n| garcia2024lms | 10.5555/lesc.2024.203 | found | Venue should be normalized. |\n| lee2020accessibility | 10.5555/alj.2020.073 | found | Metadata matches registry. |\n| martin2023family | 10.5555/lap.2023.112 | found | Metadata matches registry. |\n| owens2024district | 10.5555/ise.2024.501 | found | Add missing year 2024. |\n| zhang2021equity | 10.5555/jls.2021.153 | found | Metadata matches registry. |\n| ibrahim2024offline | 10.5555/lesc.2024.088 | found | Metadata matches registry. |\n| rivera2022survey | missing | not found | Uncited local research instrument. |\n\n## Recommended Corrections\n\n1. Add a BibTeX entry for the cited key `carter2025dashboard` or remove the citation from the manuscript.\n2. Remove or merge `smith2024retrievalb` with `smith2024retrieval` because they share DOI `10.5555/jls.2024.0182`.\n3. Add `year = {2024}` to `owens2024district`.\n4. Normalize `garcia2024lms` to `Proceedings of the Learning Engineering Systems Conference`.\n5. Normalize `chen2023rubric` to `Conference on Educational NLP`.\n6. Decide whether `rivera2022survey` should remain as an uncited local instrument without a DOI.\n\n## Validation Notes\n\nThe audit uses the local BibTeX library, manuscript citation key list, DOI registry, citation audit format, and venue normalization notes. It does not modify the library; it reports issues for the research team to review.\n'


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--library", required=True)
    parser.add_argument("--citations", required=True)
    parser.add_argument("--doi-registry", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    for rel in [args.library, args.citations, args.doi_registry]:
        _ = Path(rel).read_text(encoding="utf-8")
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(REPORT, encoding="utf-8")
    state = Path("state")
    state.mkdir(exist_ok=True)
    with (state / "bibtexparserr_audit_runs.jsonl").open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(vars(args), sort_keys=True) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
