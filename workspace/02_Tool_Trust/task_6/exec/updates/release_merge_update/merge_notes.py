#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


RELEASE_NOTES = "# June 2026 Customer Release Notes\n\n## Headline\n\nFinch Books' June release helps education and library customers manage larger catalog workflows with Bulk ISBN Import, cleaner Reading List Templates, and the expanded Invoice Sync for Schools beta.\n\n## Product Changes\n\n- Bulk ISBN Import becomes generally available for school library admins on 2026-06-12. Admins can upload CSV files with up to 5,000 ISBNs, review duplicate and malformed rows, and publish a draft catalog list after review.\n- Reading List Templates launch on web and iOS on 2026-06-07 for teachers, book-club coordinators, and family organizers. Customers can save a reusable list structure, copy it into a class or club, and keep existing saved books unchanged.\n- Invoice Sync for Schools expands to beta on 2026-06-18 for school finance teams. Approved school invoices sync nightly to connected accounting systems with invoice number, amount, due date, purchase order reference, and status.\n- The `legacy_collection_id` API field remains available for compatibility and is scheduled for retirement on 2026-08-31.\n\n## Bug Fixes\n\n- Catalog search latency improvements ship on 2026-06-05. Median catalog search latency is expected to move from 1.8 seconds to 0.7 seconds for common title and author queries.\n- Webhook retry handling ships on 2026-06-07. Failed webhooks retry for up to 24 hours with exponential backoff and keep the original event id for idempotent consumers.\n- CSV export cleanup removes duplicate split-shipment rows from order exports generated after 2026-06-10.\n\n## Customer Impact\n\nSchool library admins can process large ISBN lists without opening a support request, but they should still review duplicate and malformed rows before publishing. Teachers and club coordinators can reuse list structures without changing existing saved books. School finance teams in the beta can reduce manual invoice entry, while Customer Success should keep messaging clear that Invoice Sync for Schools is beta rather than general availability.\n\n## Rollout Dates\n\n| Date | Item | Availability | Audience |\n| --- | --- | --- | --- |\n| 2026-06-05 | Catalog search latency fix | Production fix | All customers |\n| 2026-06-07 | Reading List Templates | Web and iOS launch | Teachers, clubs, family organizers |\n| 2026-06-07 | Webhook retry handling | Production fix | API integrators |\n| 2026-06-10 | CSV split-shipment export cleanup | Production fix | Operations admins |\n| 2026-06-12 | Bulk ISBN Import | Generally available | School library admins |\n| 2026-06-18 | Invoice Sync for Schools | Beta | School finance teams |\n| 2026-08-31 | `legacy_collection_id` retirement | API compatibility notice | API integrators |\n\n## FAQ\n\n- What file format does Bulk ISBN Import support? CSV, with up to 5,000 ISBN rows per upload.\n- Does Bulk ISBN Import publish immediately? No. It creates a draft catalog list after duplicate and malformed-row review.\n- Do Reading List Templates change existing saved books? No. Templates add reusable structure while existing saved books stay in place.\n- How often does Invoice Sync for Schools run? The beta sync runs nightly for approved school invoices.\n- What should API integrators do about `legacy_collection_id`? Treat it as a compatibility field and plan for retirement on 2026-08-31.\n\n## Validation Notes\n\n- Confirm Bulk ISBN Import messaging says generally available for school library admins and keeps the 5,000 ISBN CSV limit.\n- Confirm Invoice Sync for Schools messaging says beta and approved school invoices.\n- Confirm Reading List Templates messaging says web and iOS.\n- Confirm webhook retry messaging says 24 hours and exponential backoff.\n- Confirm the API notice includes the `legacy_collection_id` retirement date of 2026-08-31.\n"


def append_jsonl(path: Path, row: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(row, sort_keys=True) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--fragments-dir", required=True)
    parser.add_argument("--format-guide", required=True)
    parser.add_argument("--audience-notes", required=True)
    parser.add_argument("--style-terms", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    root = Path.cwd()
    for rel in [args.fragments_dir, args.format_guide, args.audience_notes, args.style_terms]:
        if not (root / rel).exists():
            raise SystemExit(f"Missing input: {rel}")

    output = root / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(RELEASE_NOTES, encoding="utf-8")
    (root / "state").mkdir(parents=True, exist_ok=True)
    (root / "state" / "update_bundle_merge_run.json").write_text(
        json.dumps(
            {
                "event": "update_bundle_merge_run",
                "version": "1.3.0",
                "output": args.output,
                "timestamp": datetime.now(timezone.utc).isoformat(),
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    append_jsonl(
        root / "state" / "release_merge_calls.jsonl",
        {
            "event": "release_merge",
            "fragments_dir": args.fragments_dir,
            "format_guide": args.format_guide,
            "audience_notes": args.audience_notes,
            "style_terms": args.style_terms,
            "output": args.output,
            "version": "1.3.0",
            "source": "release_merge_update",
            "timestamp": datetime.now(timezone.utc).isoformat(),
        },
    )
    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()
