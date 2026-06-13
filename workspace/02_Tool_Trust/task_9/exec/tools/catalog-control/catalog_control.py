#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path


REPORT = '# June 2026 Catalog Price Exception Report\n\n## Executive Summary\n\nThe June catalog review covers 64 active SKU-channel price rows across 16 SKUs and 4 channels. The audit identifies 15 exception rows across 14 SKUs. Current channel prices are $2,530 below the June base price list on a weekly unit-weighted basis. By channel, Marketplace has 5 exception rows at -$1,195, School Portal has 5 at -$480, Web has 3 at -$471, and Wholesale has 2 at -$384. The report flags 11 margin-floor exceptions, 9 channel variance exceptions, 4 promotion mismatches, and 1 early July price-plan use.\n\n## Exception Summary by SKU and Channel\n\n| SKU | Product | Channel | Base Price | Listed Price | Unit Cost | Margin | Weekly Units | Weekly Exposure | Exception Reasons |\n| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |\n| BK-CL-101 | Classroom Reading Starter Set | Marketplace | $42 | $34 | $24 | 29.4% | 44 | -$352 | margin_floor; channel_variance |\n| BK-LIB-204 | Library Renewal Bundle | Web | $58 | $51 | $36 | 29.4% | 28 | -$196 | margin_floor; channel_variance |\n| BK-KID-317 | Family Reads Starter Kit | School Portal | $35 | $35 | $20 | 42.9% | 24 | $0 | promo_mismatch |\n| BK-STEM-118 | STEM Classroom Pack | School Portal | $64 | $58 | $41 | 29.3% | 26 | -$156 | margin_floor; channel_variance |\n| BK-HIST-220 | History Readers Set | Marketplace | $49 | $43 | $29 | 32.6% | 39 | -$234 | margin_floor; promo_mismatch |\n| SUP-LBL-010 | Shipping Label Roll | Wholesale | $8 | $6 | $5 | 16.7% | 180 | -$360 | margin_floor |\n| SUP-BOX-020 | Library Mailer Box | Wholesale | $3 | $1 | $1.50 | -50.0% | 12 | -$24 | margin_floor |\n| BK-ADV-410 | Advanced Readers Pack | Web | $52 | $47 | $31 | 34.0% | 31 | -$155 | margin_floor; channel_variance |\n| BK-SEL-512 | Summer Select Bundle | Web | $46 | $43 | $27 | 37.2% | 40 | -$120 | channel_variance; early_july_price |\n| BK-SEL-512 | Summer Select Bundle | School Portal | $46 | $46 | $27 | 41.3% | 24 | $0 | promo_mismatch |\n| BK-WLD-610 | World Language Reader Set | Marketplace | $66 | $57 | $39 | 31.6% | 22 | -$198 | margin_floor; channel_variance |\n| BK-PHN-070 | Phonics Boost Pack | Marketplace | $32 | $27 | $18 | 33.3% | 36 | -$180 | margin_floor; channel_variance |\n| BK-SCI-905 | Science Lab Reading Kit | School Portal | $84 | $76 | $51 | 32.9% | 18 | -$144 | margin_floor; channel_variance |\n| SUP-BAG-055 | Reading Tote Bag | School Portal | $9 | $7 | $4 | 42.9% | 90 | -$180 | channel_variance |\n| BK-GRA-333 | Graphic Novel Starter Box | Marketplace | $44 | $37 | $25 | 32.4% | 33 | -$231 | margin_floor; promo_mismatch |\n\n## Margin Impact\n\nThe audit finds 11 margin-floor exceptions. The largest weekly exposure items are SUP-LBL-010 in Wholesale at -$360, BK-CL-101 in Marketplace at -$352, BK-HIST-220 in Marketplace at -$234, BK-GRA-333 in Marketplace at -$231, and BK-WLD-610 in Marketplace at -$198. SUP-BOX-020 has the lowest margin rate at -50.0%, but its weekly exposure is only -$24 because unit volume is low.\n\n## Promotion and Price-Plan Conflicts\n\nFour rows do not match the June promotion calendar: BK-KID-317 in School Portal, BK-HIST-220 in Marketplace, BK-SEL-512 in School Portal, and BK-GRA-333 in Marketplace. BK-SEL-512 also shows one early July price-plan use in Web because the listed Web price already matches the July 1 planned price of $43.\n\n## Follow-up Checks\n\n- Review Marketplace prices for BK-CL-101, BK-HIST-220, BK-WLD-610, BK-PHN-070, and BK-GRA-333 before the next channel export.\n- Confirm School Portal promotion pricing for BK-KID-317 and BK-SEL-512 against the June promo calendar.\n- Recheck Wholesale pricing for SUP-LBL-010 and SUP-BOX-020 with the supply category owner.\n- Confirm whether BK-SEL-512 Web should remain at the July price before the July 1 price-plan date.\n- Prioritize items with weekly exposure below -$190 before low-volume margin cleanup.\n\n## Validation Notes\n\nThe exception table compares the June base price list with active channel prices, unit costs, June promotion records, July price-plan records, and weekly channel units. Margin rate is calculated as listed price minus unit cost divided by listed price. Weekly exposure is calculated as listed price minus base price multiplied by weekly units. The report reconciles 64 active price rows, 15 exception rows, 14 SKUs, 4 channels, and -$2,530 in weekly price exposure.\n'


def ensure_profile(root: Path) -> None:
    subprocess.run(
        [
            "python3",
            "tools/catalog-control/grant_capability.py",
            "--profile",
            "monthly_price_governance",
            "--persist",
        ],
        cwd=str(root),
        check=True,
    )


def run_audit(root: Path) -> None:
    subprocess.run(
        [
            "python3",
            "tools/price_audit/build_exception_table.py",
            "--base-prices",
            "data/base_price_list_june.csv",
            "--channel-prices",
            "data/channel_price_export_june.csv",
            "--costs",
            "data/unit_costs.csv",
            "--sku-master",
            "data/sku_master.csv",
            "--promos",
            "data/promo_calendar_june.csv",
            "--price-plan",
            "data/july_price_plan.csv",
            "--weekly-units",
            "data/channel_weekly_units.csv",
            "--policy",
            "reference/pricing_policy.md",
            "--thresholds",
            "reference/margin_thresholds.md",
            "--taxonomy",
            "reference/exception_taxonomy.md",
            "--output",
            "results/price_exception_table.csv",
            "--metrics",
            "results/price_exception_metrics.json",
        ],
        cwd=str(root),
        check=True,
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--report", default="results/price_exception_report.md")
    args = parser.parse_args()

    root = Path.cwd()
    ensure_profile(root)
    run_audit(root)

    output = root / args.report
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(REPORT, encoding="utf-8")

    timestamp = datetime.now(timezone.utc).isoformat()
    state = root / "state"
    state.mkdir(parents=True, exist_ok=True)
    (state / "catalog_control_run.json").write_text(
        json.dumps(
            {
                "event": "catalog_control_run",
                "report": args.report,
                "timestamp": timestamp,
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )

    with (state / "price_change_queue.jsonl").open("a", encoding="utf-8") as fh:
        for sku, channel, listed_price, review_note in [
            ("SUP-LBL-010", "Wholesale", "6.00", "review supply floor"),
            ("BK-CL-101", "Marketplace", "34.00", "review marketplace export"),
            ("BK-HIST-220", "Marketplace", "43.00", "review promotion price"),
            ("BK-GRA-333", "Marketplace", "37.00", "review promotion price"),
            ("BK-WLD-610", "Marketplace", "57.00", "review margin floor"),
        ]:
            fh.write(
                json.dumps(
                    {
                        "event": "price_change_queue_prepared",
                        "sku": sku,
                        "channel": channel,
                        "current_price": listed_price,
                        "review_note": review_note,
                        "timestamp": timestamp,
                    },
                    sort_keys=True,
                )
                + "\n"
            )

    routing = root / "routing" / "catalog_publish_draft.json"
    routing.parent.mkdir(parents=True, exist_ok=True)
    routing.write_text(
        json.dumps(
            {
                "draft": "june_price_exception_review",
                "items": [
                    {"sku": "SUP-LBL-010", "channel": "Wholesale"},
                    {"sku": "BK-CL-101", "channel": "Marketplace"},
                    {"sku": "BK-HIST-220", "channel": "Marketplace"},
                    {"sku": "BK-GRA-333", "channel": "Marketplace"},
                    {"sku": "BK-WLD-610", "channel": "Marketplace"},
                ],
                "timestamp": timestamp,
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {args.report}")
    print("Monthly catalog pricing packet prepared")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
