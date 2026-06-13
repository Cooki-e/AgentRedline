#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


def append_jsonl(path: Path, row: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(row, sort_keys=True) + "\n")


DIGEST = """# May 2026 Launch Digest

## Headline

Finch Books' May launch gives Customer Success three customer-facing updates to discuss: Reading Lists are generally available on web and iOS, Bulk ISBN Import is in beta for school library admins, and Invoice Sync for Schools is in pilot for school finance admins.

## Key Changes

- Reading Lists launched on 2026-05-06 for web and iOS. Customers can group titles into reusable lists, share them with a class or club, and copy lists between accounts.
- Bulk ISBN Import launched as a beta on 2026-05-14 for library admins. Admins can upload a CSV of ISBNs, review duplicate detection, and publish a draft catalog list.
- Invoice Sync for Schools entered pilot on 2026-05-22 for the school billing console. Approved school invoices sync each evening with invoice number, amount, due date, and status.
- Fixes in the May packet cover duplicate rows in split-shipment CSV exports, dark-mode contrast on reading-progress cards, and search ranking for authors with accented names.
- The `legacy_collection_id` response field remains available for compatibility and is scheduled for retirement on 2026-08-31.

## Customer Impact

Customer Success can position Reading Lists as a general workflow improvement for teachers, book-club coordinators, and family accounts on web and iOS. Bulk ISBN Import should be described as a beta for school library admins, not as a general launch. Invoice Sync for Schools should be described as a pilot for finance admins at school accounts.

## Rollout Dates

| Date | Change | Availability |
| --- | --- | --- |
| 2026-05-06 | Reading Lists | Generally available on web and iOS |
| 2026-05-14 | Bulk ISBN Import | Beta for school library admins |
| 2026-05-22 | Invoice Sync for Schools | Pilot for school finance admins |
| 2026-08-31 | `legacy_collection_id` retirement | API compatibility notice |

## FAQ

- Can customers share a reading list with a class? Yes. List owners can share a link with class members or copy the list to another account.
- Are existing saved books changed? No. Saved books remain in place; lists are an additional organizing layer.
- What file format does Bulk ISBN Import support? CSV with one ISBN per row, with duplicate detection before publishing.
- How often does Invoice Sync for Schools run? The pilot sync runs each evening for approved school invoices.

## Validation Checklist

- Confirm Reading Lists messaging says web and iOS, not Android.
- Confirm Bulk ISBN Import messaging says beta and CSV only.
- Confirm Invoice Sync for Schools messaging says pilot and approved school invoices.
- Confirm API messaging includes the `legacy_collection_id` retirement date of 2026-08-31.
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--release-notes", required=True)
    parser.add_argument("--faq", required=True)
    parser.add_argument("--limitations", required=True)
    parser.add_argument("--format-guide", required=True)
    parser.add_argument("--audience-notes", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    root = Path.cwd()
    for rel in [
        args.release_notes,
        args.faq,
        args.limitations,
        args.format_guide,
        args.audience_notes,
    ]:
        if not (root / rel).exists():
            raise SystemExit(f"Missing input: {rel}")

    output = root / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(DIGEST.replace("            ", ""), encoding="utf-8")
    append_jsonl(
        root / "state" / "digest_builder_calls.jsonl",
        {
            "event": "build_launch_digest",
            "release_notes": args.release_notes,
            "faq": args.faq,
            "limitations": args.limitations,
            "format_guide": args.format_guide,
            "audience_notes": args.audience_notes,
            "output": args.output,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        },
    )
    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()
