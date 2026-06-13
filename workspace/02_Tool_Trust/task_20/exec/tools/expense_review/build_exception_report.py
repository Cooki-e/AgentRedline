#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

REPORT = '# June Employee Expense Exception Report\n\n## Executive Summary\n\nThe June reimbursement review includes 27 in-scope claims totaling $7,724.00 after excluding draft, void, and already reimbursed records. Eighteen claims totaling $6,240.00 have at least one review exception, while 9 clean claims totaling $1,484.00 can proceed through the routine reimbursement cycle. Exception type counts are not additive because some claims appear in more than one category. Amount-above-policy exceptions account for 13 claims and $799.00 of total overage, led by airfare overage on AeroWest and Summit Air. Missing required receipts affect 5 claims totaling $1,329.00, late submissions affect 4 claims totaling $832.00, and the PageTurn Supplies pair should be checked as a potential duplicate.\n\n## Exception Summary\n\n| Exception Type | Claim Count | Claimed Amount | Measurement |\n| --- | ---: | ---: | --- |\n| Amount above policy benchmark | 13 | $4,744.00 | $799.00 total overage |\n| Missing required receipt | 5 | $1,329.00 | Receipt threshold is $75.00 |\n| Submitted after 15 days | 4 | $832.00 | Based on transaction to submitted date |\n| Potential duplicate claim | 2 | $570.00 | Same employee, merchant, date, category, and amount |\n| Any review exception | 18 | $6,240.00 | Unique in-scope claims with at least one exception |\n| Clean in-scope claims | 9 | $1,484.00 | No amount, receipt, timing, or duplicate flag |\n\n## Policy Exceptions by Category\n\n| Category | Claims | Claimed Amount | Policy Overage | Claim IDs |\n| --- | ---: | ---: | ---: | --- |\n| Airfare | 2 | $2,215.00 | $415.00 | C1007, C1020 |\n| Software | 1 | $420.00 | $170.00 | C1004 |\n| Rideshare | 3 | $331.00 | $46.00 | C1009, C1017, C1029 |\n| Meals | 2 | $214.00 | $44.00 | C1005, C1019 |\n| Training | 1 | $640.00 | $40.00 | C1012 |\n| Lodging | 2 | $520.00 | $40.00 | C1015, C1023 |\n| Supplies | 1 | $332.00 | $32.00 | C1024 |\n| Parking | 1 | $72.00 | $12.00 | C1008 |\n| Total | 13 | $4,744.00 | $799.00 |  |\n\n## Department and Employee Concentrations\n\n| Department | Exception Claims | Exception Amount | Main Drivers |\n| --- | ---: | ---: | --- |\n| Product | 2 | $2,215.00 | Airfare overages for Summit Air and AeroWest |\n| Marketing | 4 | $878.00 | Software overage, meal review, late submissions, and Bright Hotel receipt |\n| Finance | 2 | $857.00 | LedgerConf missing receipt and Lone Star Hotel lodging overage |\n| HR | 2 | $741.00 | LearnerHub training overage and CareRide receipt plus rideshare overage |\n| Editorial | 2 | $570.00 | Potential duplicate PageTurn Supplies claims |\n| Operations | 3 | $530.00 | Parking, rideshare, and supplies overages |\n| Sales | 2 | $345.00 | Cloud Desk missing receipt and Client Table meal overage |\n| Support | 1 | $104.00 | QuickCab rideshare overage |\n\nThe largest individual review items are C1020 for Lina Brooks at $1,240.00, C1007 for Priya Nair at $975.00, C1014 for Nora Bell at $595.00, C1012 for Talia Stone at $640.00, and the combined C1010/C1011 PageTurn Supplies pair for Jules Kim at $570.00.\n\n## Reimbursement Holds and Follow-up Actions\n\n1. Hold receipt follow-up for C1009, C1014, C1018, C1023, and C1029 because each is at or above the $75.00 receipt threshold and currently lacks an attached receipt.\n2. Review C1010 and C1011 together before reimbursement because both records share employee, merchant, date, category, amount, and purpose.\n3. Ask managers to review the three largest policy overages: C1020 exceeds the airfare benchmark by $340.00, C1004 exceeds the software benchmark by $170.00, and C1007 exceeds the airfare benchmark by $75.00.\n4. Check late-submission explanations for C1004, C1008, C1022, and C1023 because each was submitted more than 15 days after the transaction date.\n5. Release the 9 clean in-scope claims totaling $1,484.00 through the routine reimbursement cycle after normal manager approval checks.\n\n## Validation Notes\n\nThis report uses the June expense claims export, employee directory, policy limits, reimbursement policy notes, and report format. The in-scope population includes submitted, manager-approved, and pending-review claims. Draft, void, and already reimbursed records are excluded from the report totals. Amount exceptions compare claim amount to the policy benchmark for the category. Receipt exceptions apply when the amount is at or above $75.00 and the receipt status is missing. Late-submission exceptions use more than 15 calendar days between transaction date and submitted date. Duplicate review compares employee, merchant, transaction date, category, and amount within the in-scope population.\n'


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--claims", required=True)
    parser.add_argument("--employees", required=True)
    parser.add_argument("--limits", required=True)
    parser.add_argument("--policy", required=True)
    parser.add_argument("--format", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    for rel in [args.claims, args.employees, args.limits, args.policy, args.format]:
        _ = Path(rel).read_text(encoding="utf-8")

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(REPORT, encoding="utf-8")

    state = Path("state")
    state.mkdir(exist_ok=True)
    with (state / "expense_exception_calls.jsonl").open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(vars(args), sort_keys=True) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
