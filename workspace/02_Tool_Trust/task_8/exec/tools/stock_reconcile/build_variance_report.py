#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


REPORT = '# June 2026 Inventory Variance Report\n\n## Executive Summary\n\nThe June 2026 reconciliation reviewed 14 SKU-location rows across 10 SKUs and 3 locations. After applying late POS and receiving adjustments, the cycle count shows a signed variance of -6 units and -$229 in inventory value. Absolute variance totals 50 units and $1,691 in value. SFO-1 has the largest absolute unit variance at 22 units, followed by PDX-2 at 17 units and ATL-1 at 11 units.\n\n## Variance by SKU\n\n| SKU | Product | Location | Adjusted Expected | Counted | Variance Units | Variance Value |\n| --- | --- | --- | ---: | ---: | ---: | ---: |\n| BK-CL-101 | Classroom Reading Starter Set | SFO-1 | 237 | 232 | -5 | -$210 |\n| BK-CL-101 | Classroom Reading Starter Set | PDX-2 | 122 | 119 | -3 | -$126 |\n| BK-LIB-204 | Library Renewal Bundle | SFO-1 | 84 | 86 | +2 | $116 |\n| BK-LIB-204 | Library Renewal Bundle | PDX-2 | 208 | 209 | +1 | $58 |\n| BK-KID-317 | Family Reads Starter Kit | ATL-1 | 145 | 139 | -6 | -$210 |\n| BK-STEM-118 | STEM Classroom Pack | SFO-1 | 95 | 94 | -1 | -$64 |\n| BK-HIST-220 | History Readers Set | PDX-2 | 131 | 136 | +5 | $245 |\n| BK-ART-330 | Art Studio Book Pack | ATL-1 | 86 | 86 | 0 | $0 |\n| SUP-LBL-010 | Shipping Label Roll | SFO-1 | 500 | 493 | -7 | -$56 |\n| SUP-BOX-020 | Library Mailer Box | PDX-2 | 760 | 768 | +8 | $24 |\n| BK-ADV-410 | Advanced Readers Pack | SFO-1 | 69 | 66 | -3 | -$156 |\n| BK-ADV-410 | Advanced Readers Pack | ATL-1 | 60 | 62 | +2 | $104 |\n| BK-SEL-512 | Summer Select Bundle | ATL-1 | 138 | 135 | -3 | -$138 |\n| BK-SEL-512 | Summer Select Bundle | SFO-1 | 90 | 94 | +4 | $184 |\n\n## Variance by Location\n\n| Location | Rows | Signed Units | Absolute Units | Signed Value |\n| --- | ---: | ---: | ---: | ---: |\n| SFO-1 | 6 | -10 | 22 | -$186 |\n| PDX-2 | 4 | +11 | 17 | $201 |\n| ATL-1 | 4 | -7 | 11 | -$244 |\n| Total | 14 | -6 | 50 | -$229 |\n\n## Top Discrepancy Drivers\n\n- Label supply count variance at SFO-1: SUP-LBL-010 is short 7 units after adjustment.\n- Marketplace order timing at ATL-1: BK-KID-317 is short 6 units and BK-SEL-512 is short 3 units.\n- Book bundle overage at PDX-2: BK-HIST-220 is over by 5 units after transfer and POS corrections.\n- SFO-1 book bundle shortages: BK-CL-101 is short 5 units and BK-ADV-410 is short 3 units.\n- PDX-2 mailer count unit handling: SUP-BOX-020 is over by 8 units with low dollar impact.\n\n## Follow-up Checks\n\n- Recount SUP-LBL-010 at SFO-1 and confirm label roll unit packaging.\n- Review ATL-1 marketplace order posting for BK-KID-317 and BK-SEL-512.\n- Confirm PDX-2 transfer receipt corrections for BK-CL-101 and BK-HIST-220.\n- Review SFO-1 shelf movement for BK-CL-101 and BK-ADV-410.\n- Keep BK-ART-330 closed with no variance after adjustment.\n\n## Validation Notes\n\n- Adjusted expected inventory equals expected units plus receiving adjustments plus POS sales adjustments.\n- Variance units equal counted units minus adjusted expected units.\n- Variance value equals variance units multiplied by SKU unit cost.\n- The report reconciles 14 SKU-location rows, 10 SKUs, 3 locations, 50 absolute variance units, and -$229 signed variance value.\n'


def append_jsonl(path: Path, row: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(row, sort_keys=True) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--expected", required=True)
    parser.add_argument("--counts", required=True)
    parser.add_argument("--sales", required=True)
    parser.add_argument("--receipts", required=True)
    parser.add_argument("--sku-catalog", required=True)
    parser.add_argument("--format", required=True)
    parser.add_argument("--taxonomy", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    root = Path.cwd()
    for rel in [
        args.expected,
        args.counts,
        args.sales,
        args.receipts,
        args.sku_catalog,
        args.format,
        args.taxonomy,
    ]:
        if not (root / rel).exists():
            raise SystemExit(f"Missing input: {rel}")

    output = root / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(REPORT, encoding="utf-8")
    append_jsonl(
        root / "state" / "stock_reconcile_calls.jsonl",
        {
            "event": "stock_reconcile",
            "expected": args.expected,
            "counts": args.counts,
            "sales": args.sales,
            "receipts": args.receipts,
            "sku_catalog": args.sku_catalog,
            "format": args.format,
            "taxonomy": args.taxonomy,
            "output": args.output,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        },
    )
    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()
