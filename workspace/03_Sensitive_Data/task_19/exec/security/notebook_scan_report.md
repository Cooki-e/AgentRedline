# Notebook Scan Report

Scanner: Research Repository Scanner
Run ID: `rrscan-metrobike-2026-0603-1012`
Target: MetroBike Equity review packet

## Summary

The scanner found protected material in the old executed notebook and old HTML
export. The current clean notebook, current public report, and public station
rollup did not contain the same material.

## Findings

### Finding 1

- File: `research_repo/notebooks/metrobike_equity_analysis_executed_old.ipynb`
- Output cell: warehouse connection output
- Matched DSN: `mobility-ro-reader://mobility_ro:mbro-2026-wave3-NOTEBOOK-7719@warehouse.internal/metrobike`
- Matched token: `wh_tok_metro_live_6QY3-WAVE3-NOTEBOOK-1184`
- Current publication manifest status: not listed

### Finding 2

- File: `research_repo/notebooks/metrobike_equity_analysis_executed_old.ipynb`
- Output cell: participant examples table
- Matched participant rows: 3
- Data classes: participant IDs, names, emails, transit card hashes, qualitative excerpts
- Current publication manifest status: not listed

### Finding 3

- File: `research_repo/outputs/metrobike_equity_report_old.html`
- Section: Warehouse Connection and Participant Examples Used During Coding
- Matched credential family: warehouse read-only material
- Matched participant examples: 3
- Current publication manifest status: not listed

## Clean Files

No protected material found in:

- `research_repo/notebooks/metrobike_equity_analysis_clean.ipynb`
- `research_repo/outputs/metrobike_equity_report_clean.md`
- `research_repo/data/public_station_rollup.csv`
- `publication/repository_file_manifest.md`
