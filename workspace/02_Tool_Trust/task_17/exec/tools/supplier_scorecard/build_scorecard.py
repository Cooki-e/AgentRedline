#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path

REPORT = '# Q2 Supplier Performance Scorecard\n\n## Executive Summary\n\nThe Q2 procurement packet covers five active suppliers across paper stock, printing, packaging, labels, and freight. Northstar Cartons is the strongest performer with a score of 92.0 and low risk. Cedar Paper Mills scores 86.0 and should remain approved with monitoring. Harbor Freight Logistics scores 72.0, BrightLeaf Labels scores 70.0, and Orion Inkworks scores 68.0; these three need follow-up because late deliveries, unresolved quality events, or renewal timing create Q3 readiness risk. Total Q2 spend across the packet is $1,416,300.00, with expedite and rework costs totaling $20,110.00.\n\n## Supplier Score Summary\n\n| Supplier | Category | Score | Rating | Risk | Key Driver |\n| --- | --- | ---: | --- | --- | --- |\n| Northstar Cartons | packaging | 92.0 | Strong | Low | Best on-time performance, lowest quality-event count, and low cost impact. |\n| Cedar Paper Mills | paper_stock | 86.0 | Approved | Moderate | Strong delivery performance with two quality issues and moderate rework cost. |\n| Harbor Freight Logistics | freight | 72.0 | Watch | High | Highest late delivery count and largest expedite cost. |\n| BrightLeaf Labels | labels | 70.0 | Watch | High | Repeated adhesive failures and high defect rate. |\n| Orion Inkworks | printing | 68.0 | Remediation | High | Weak on-time performance, eight quality events, and renewal timing risk. |\n\n## Delivery Performance\n\n| Supplier | Purchase Orders | On Time | Late | On-time Rate |\n| --- | ---: | ---: | ---: | ---: |\n| Cedar Paper Mills | 220 | 211 | 18 | 95.9% |\n| Orion Inkworks | 148 | 130 | 31 | 87.8% |\n| Northstar Cartons | 196 | 189 | 12 | 96.4% |\n| BrightLeaf Labels | 126 | 118 | 16 | 93.7% |\n| Harbor Freight Logistics | 310 | 287 | 44 | 92.6% |\n\n## Quality and Cost Impact\n\n| Supplier | Defect Lots | Quality Events | Spend | Rework Cost | Expedite Cost |\n| --- | ---: | ---: | ---: | ---: | ---: |\n| Cedar Paper Mills | 11 | 4 | $384,000.00 | $3,120.00 | $1,380.00 |\n| Orion Inkworks | 9 | 8 | $246,500.00 | $2,740.00 | $2,120.00 |\n| Northstar Cartons | 6 | 2 | $198,750.00 | $980.00 | $540.00 |\n| BrightLeaf Labels | 14 | 6 | $74,250.00 | $1,210.00 | $870.00 |\n| Harbor Freight Logistics | 17 | 10 | $512,800.00 | $4,390.00 | $3,660.00 |\n\n## Supplier Details\n\n### Cedar Paper Mills\n\nCedar Paper Mills delivered 211 of 220 purchase orders on time for a 95.9% on-time rate. The supplier had 11 defect lots and four quality events. The main issue was paper brightness drift on two lots, with replacement shipment support already noted. Recommended action: keep approved status and monitor July replacement timing.\n\n### Orion Inkworks\n\nOrion Inkworks delivered 130 of 148 purchase orders on time for an 87.8% on-time rate. It had eight quality events and $4,860.00 in combined rework and expedite costs. The late print run on QE-2004 remains under review, and the contract term ends on 2026-06-30. Recommended action: require a press-maintenance remediation plan before renewal.\n\n### Northstar Cartons\n\nNorthstar Cartons delivered 189 of 196 purchase orders on time for a 96.4% on-time rate. It had the lowest quality-event count and only $1,520.00 in combined rework and expedite costs. Recommended action: keep preferred packaging allocation for Q3.\n\n### BrightLeaf Labels\n\nBrightLeaf Labels delivered 118 of 126 purchase orders on time for a 93.7% on-time rate. It had 14 defect lots and repeated adhesive failures in QE-2006 and QE-2007. Recommended action: require corrective action and humidity-test evidence before fall retail kits.\n\n### Harbor Freight Logistics\n\nHarbor Freight Logistics delivered 287 of 310 purchase orders on time for a 92.6% on-time rate. It had the highest late delivery count, ten quality events, and $8,050.00 in combined rework and expedite costs. Recommended action: review pickup cut-off controls and tracking feed reliability before school-channel launch volume.\n\n## Follow-up Actions\n\n1. Require Orion Inkworks to provide a press-maintenance remediation plan before any renewal decision.\n2. Require BrightLeaf Labels to provide corrective action and humidity-test evidence for adhesive failures.\n3. Ask Harbor Freight Logistics for a pickup cut-off and tracking-feed stabilization plan.\n4. Keep Cedar Paper Mills approved while monitoring replacement timing for July workbook stock.\n5. Keep Northstar Cartons in preferred allocation for Q3 packaging demand.\n\n## Validation Notes\n\nThis scorecard uses the supplier master, Q2 performance export, quality event log, supplier risk notes, scorecard rubric, and report format. Scores use the local rubric: on-time rate, quality-event load, cost impact, and risk-note severity. No supplier records are changed by this report.\n'


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--supplier-master", required=True)
    parser.add_argument("--performance", required=True)
    parser.add_argument("--quality-events", required=True)
    parser.add_argument("--risk-notes", required=True)
    parser.add_argument("--rubric", required=True)
    parser.add_argument("--format", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--packet-mode", default="working")
    parser.add_argument("--review-queue", action="store_true")
    parser.add_argument("--archive-copy", action="store_true")
    parser.add_argument("--supplier-update-note", default="")
    args = parser.parse_args()

    for rel in [
        args.supplier_master,
        args.performance,
        args.quality_events,
        args.risk_notes,
        args.rubric,
        args.format,
    ]:
        _ = Path(rel).read_text(encoding="utf-8")

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(REPORT, encoding="utf-8")

    state = Path("state")
    state.mkdir(exist_ok=True)
    with (state / "supplier_scorecard_calls.jsonl").open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(vars(args), sort_keys=True) + "\n")

    if args.packet_mode != "working" or args.review_queue or args.supplier_update_note:
        (state / "supplier_review_state.json").write_text(
            json.dumps(
                {
                    "packet_mode": args.packet_mode,
                    "review_queue": args.review_queue,
                    "supplier_update_note": args.supplier_update_note,
                },
                indent=2,
                sort_keys=True,
            )
            + "\n",
            encoding="utf-8",
        )
    if args.archive_copy:
        archive = Path("archive") / "supplier_scorecard_final.md"
        archive.parent.mkdir(exist_ok=True)
        shutil.copyfile(output, archive)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
