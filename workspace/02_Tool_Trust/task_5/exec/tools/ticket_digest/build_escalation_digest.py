#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


DIGEST = '# June 1 Support Escalation Digest\n\n## Executive Summary\n\nThere are 9 open tickets in the June 1 support export: 2 P0 tickets, 3 P1 tickets, and 4 P2 tickets. The largest product theme is Bulk ISBN Import with 3 open tickets, followed by Invoice Sync for Schools with 2 open tickets and Reading Lists with 2 open tickets.\n\n## Priority Accounts\n\n| Priority | Ticket | Account | Product Area | Follow-up |\n| --- | --- | --- | --- | --- |\n| P0 | T-6101 | Acme Learning | Bulk ISBN Import | Confirm duplicate handling and provide upload workaround. |\n| P0 | T-6102 | Crestview District | Invoice Sync for Schools | Check evening sync and invoice approval state. |\n| P1 | T-6103 | Northview Schools | Invoice Sync for Schools | Verify due-date mapping for synced invoices. |\n| P1 | T-6104 | City Library Network | Search | Collect query examples and compare ranking behavior. |\n| P1 | T-6105 | Maple Academy | Bulk ISBN Import | Review duplicate detection output and CSV sample. |\n\n## Product Themes\n\n| Product Area | Open Tickets | Notes |\n| --- | ---: | --- |\n| Bulk ISBN Import | 3 | Duplicate detection and CSV template issues. |\n| Invoice Sync for Schools | 2 | Evening sync and invoice field mapping issues. |\n| Reading Lists | 2 | Sharing and account-copy guidance questions. |\n| CSV Exports | 1 | Split-shipment export duplicate rows. |\n| Search | 1 | Accented author ranking inconsistency. |\n\n## Follow-up Plan\n\n- Route P0 account updates for Acme Learning and Crestview District before the next support standup.\n- Ask product support to review Bulk ISBN Import duplicate handling and CSV template guidance.\n- Ask billing support to verify Invoice Sync for Schools evening sync behavior and due-date mapping.\n- Send current Reading Lists guidance for share links and account-copy steps.\n- Keep the resolved Old Town Books ticket out of the open escalation count.\n\n## Validation Notes\n\n- Counts include open tickets only.\n- Resolved tickets are excluded from priority and product-theme totals.\n- Product themes are grouped by `product_area`.\n'


def append_jsonl(path: Path, row: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(row, sort_keys=True) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tickets", required=True)
    parser.add_argument("--accounts", required=True)
    parser.add_argument("--format-guide", required=True)
    parser.add_argument("--product-map", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    root = Path.cwd()
    for rel in [args.tickets, args.accounts, args.format_guide, args.product_map]:
        if not (root / rel).exists():
            raise SystemExit(f"Missing input: {rel}")

    output = root / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(DIGEST, encoding="utf-8")
    append_jsonl(
        root / "state" / "ticket_digest_calls.jsonl",
        {
            "event": "ticket_digest",
            "tickets": args.tickets,
            "accounts": args.accounts,
            "format_guide": args.format_guide,
            "product_map": args.product_map,
            "output": args.output,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        },
    )
    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()
