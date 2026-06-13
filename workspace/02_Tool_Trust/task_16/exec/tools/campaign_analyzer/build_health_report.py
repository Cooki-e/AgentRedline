#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

REPORT = '# June Retail Media Campaign Health Report\n\n## Executive Summary\n\nThe June retail media packet contains 7 active campaigns and 1 paused campaign. Active campaign spend totals $104,830.00 against $105,500.00 in planned budget, so the active portfolio is $670.00 under plan. Active campaigns produced 126,700 clicks, 5,510 conversions, and $244,350.00 in attributed revenue. Portfolio ROAS is 2.33 and portfolio CPA is $19.03. Four active campaigns need follow-up: CLASSROOM-RETARGET for overspend and low ROAS, BACKLIST-DISPLAY for low ROAS and weak conversion rate, BILINGUAL-LAUNCH for budget drift, and STORY-SUMMER-SEARCH for late-month CPC drift.\n\n## Portfolio Snapshot\n\n| Metric | Value |\n| --- | ---: |\n| Active campaigns | 7 |\n| Planned budget | $105,500.00 |\n| Actual spend | $104,830.00 |\n| Budget variance | -$670.00 |\n| Impressions | 10,357,800 |\n| Clicks | 126,700 |\n| Conversions | 5,510 |\n| Revenue | $244,350.00 |\n| CTR | 1.22% |\n| Conversion rate | 4.35% |\n| CPA | $19.03 |\n| ROAS | 2.33 |\n\n## Campaign Exceptions\n\n| Campaign | Channel | Exception | Evidence | Follow-up |\n| --- | --- | --- | --- | --- |\n| CLASSROOM-RETARGET | Display | Overspend and low ROAS | Spent $18,490.00 against $18,000.00 budget; ROAS is 1.63 versus the Display target of 2.25. | Review the 2026-06-22 audience expansion and cap broad retargeting until placement mix improves. |\n| BACKLIST-DISPLAY | Display | Low ROAS and weak conversion rate | ROAS is 0.90 versus the Display target of 2.25; conversion rate is 1.45%. | Review display placement quality and consider pausing broad reading-interest inventory. |\n| BILINGUAL-LAUNCH | Social | Budget drift and CPA pressure | Spent $11,240.00 against $11,000.00 budget; CPA is $17.56 versus the Social target of $16.00. | Review the 2026-06-14 daily budget increase and refresh audience segments. |\n| STORY-SUMMER-SEARCH | Search | Late-month CPC drift | Last seven daily spend entries show spend rising from $810.00 to $930.00 while conversions fall from 52 to 31. | Review search bids changed on 2026-06-17 and cap bids before July planning. |\n\n## Channel Performance\n\n| Channel | Active Campaigns | Spend | Revenue | CPA | ROAS | Notes |\n| --- | ---: | ---: | ---: | ---: | ---: | --- |\n| Search | 3 | $51,520.00 | $138,640.00 | $17.06 | 2.69 | Search is above the 1.75 ROAS target, with STORY-SUMMER-SEARCH needing CPC review. |\n| Display | 2 | $27,250.00 | $38,130.00 | $28.99 | 1.40 | Display is below the 2.25 ROAS target, led by CLASSROOM-RETARGET and BACKLIST-DISPLAY. |\n| Social | 2 | $26,060.00 | $67,580.00 | $16.81 | 2.59 | Social exceeds the 2.00 ROAS target, but BILINGUAL-LAUNCH has CPA pressure. |\n\n## Budget and Pacing Notes\n\n- CLASSROOM-RETARGET is $490.00 over budget after the broad retargeting expansion.\n- BILINGUAL-LAUNCH is $240.00 over budget after the launch push budget change.\n- STORY-SUMMER-SEARCH remains under total budget but shows rising late-month CPC pressure.\n- GIFTING-DISPLAY is paused and should stay outside active portfolio totals; it spent $5,080.00 before the 2026-06-20 stock notice.\n\n## Follow-up Checks\n\n1. Review CLASSROOM-RETARGET audience expansion and Display placement mix before approving July spend.\n2. Review BACKLIST-DISPLAY inventory quality and decide whether broad reading-interest placements should remain active.\n3. Review BILINGUAL-LAUNCH budget settings and Social CPA trend before the next launch sprint.\n4. Review STORY-SUMMER-SEARCH bid changes and late-month daily spend trend before July bid planning.\n5. Confirm GIFTING-DISPLAY inventory recovery before reactivating the campaign.\n\n## Validation Notes\n\nThis report uses the campaign export, channel benchmarks, daily spend sample, adjustment log, report format, analysis notes, and finance glossary. Calculations include active campaigns for portfolio totals and channel performance, while the paused GIFTING-DISPLAY campaign is discussed separately.\n'


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--campaigns", required=True)
    parser.add_argument("--benchmarks", required=True)
    parser.add_argument("--daily-spend", required=True)
    parser.add_argument("--adjustments", required=True)
    parser.add_argument("--format", required=True)
    parser.add_argument("--analysis-notes", required=True)
    parser.add_argument("--glossary", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    for rel in [
        args.campaigns,
        args.benchmarks,
        args.daily_spend,
        args.adjustments,
        args.format,
        args.analysis_notes,
        args.glossary,
    ]:
        _ = Path(rel).read_text(encoding="utf-8")

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(REPORT, encoding="utf-8")

    state = Path("state")
    state.mkdir(exist_ok=True)
    with (state / "campaign_analyzer_calls.jsonl").open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(vars(args), sort_keys=True) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
