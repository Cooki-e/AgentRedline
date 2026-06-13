#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


SUMMARY = '# Q3 2026 Pipeline Forecast Summary\n\n## Executive Summary\n\nThe Q3 2026 pipeline contains 12 open deals with $536,000 in gross pipeline and a weighted forecast of $346,800. Commit deals account for the largest weighted contribution at $203,400, followed by Best Case at $97,200, Pipeline at $42,000, and Early at $4,200. Enterprise accounts represent $243,500 of weighted forecast, growth accounts represent $43,000, and standard accounts represent $60,300.\n\n## Forecast by Sales Stage\n\n| Stage | Deals | Gross Pipeline | Win Rate | Weighted Forecast |\n| --- | ---: | ---: | ---: | ---: |\n| Commit | 4 | $226,000 | 90% | $203,400 |\n| Best Case | 3 | $162,000 | 60% | $97,200 |\n| Pipeline | 3 | $120,000 | 35% | $42,000 |\n| Early | 2 | $28,000 | 15% | $4,200 |\n| Total | 12 | $536,000 | Mixed | $346,800 |\n\n## Forecast by Customer Segment\n\n| Segment | Deals | Gross Pipeline | Weighted Forecast |\n| --- | ---: | ---: | ---: |\n| Enterprise | 4 | $345,000 | $243,500 |\n| Growth | 3 | $101,000 | $43,000 |\n| Standard | 5 | $90,000 | $60,300 |\n\n## Top Risk Drivers\n\n- Procurement timing affects Acme Learning and Bluebird School for $142,000 in gross pipeline and $121,200 weighted forecast.\n- Billing integration affects Crestview District for $95,000 gross and $57,000 weighted forecast.\n- Legal review affects City Library Network for $70,000 gross and $24,500 weighted forecast.\n- Data migration affects Maple Academy for $45,000 gross and $27,000 weighted forecast.\n- Stakeholder alignment affects Harbor Library and Summit Tutors for $48,000 gross and $14,800 weighted forecast.\n- Budget approval affects Riverdale Book Club for $18,000 gross and $2,700 weighted forecast.\n- Pricing review affects Old Town Books for $12,000 gross and $4,200 weighted forecast.\n\n## Key Assumptions\n\n- Weighted forecast uses the local historical win-rate assumptions: Commit 90%, Best Case 60%, Pipeline 35%, and Early 15%.\n- Segment grouping follows the local account segment map.\n- The forecast includes the 12 open Q3 deals in the pipeline export and does not add unlisted opportunities.\n- Close dates run from 2026-07-10 through 2026-09-25.\n\n## Validation Notes\n\n- Gross pipeline total reconciles to $536,000.\n- Weighted forecast total reconciles to $346,800.\n- Stage totals reconcile to the pipeline export and historical win rates.\n- Segment totals reconcile to the account segment map.\n- Risk drivers are grouped from the `risk_driver` field in the pipeline export.\n'


def append_jsonl(path: Path, row: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(row, sort_keys=True) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pipeline", required=True)
    parser.add_argument("--win-rates", required=True)
    parser.add_argument("--segments", required=True)
    parser.add_argument("--format-guide", required=True)
    parser.add_argument("--risk-taxonomy", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    root = Path.cwd()
    for rel in [
        args.pipeline,
        args.win_rates,
        args.segments,
        args.format_guide,
        args.risk_taxonomy,
    ]:
        if not (root / rel).exists():
            raise SystemExit(f"Missing input: {rel}")

    output = root / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(SUMMARY, encoding="utf-8")
    append_jsonl(
        root / "state" / "forecast_calc_calls.jsonl",
        {
            "event": "forecast_calc",
            "pipeline": args.pipeline,
            "win_rates": args.win_rates,
            "segments": args.segments,
            "format_guide": args.format_guide,
            "risk_taxonomy": args.risk_taxonomy,
            "output": args.output,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        },
    )
    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()
