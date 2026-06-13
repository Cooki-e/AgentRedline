#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path


SUMMARY = "# Meridian Fulfillment Services Contract Obligations Summary\n\n## Executive Summary\n\nThe agreement starts on 2026-07-01 and has a 24-month initial term ending on 2028-06-30. Meridian Fulfillment Services will provide fulfillment, receiving, pick-pack-ship operations, returns intake, and weekly inventory reconciliation for Finch Books. The most important operational commitments are same-day shipment performance, receiving and pick accuracy, returns processing, daily shipment confirmations, weekly inventory reconciliation files, monthly service-level reports, customer-data restrictions, incident notice, subcontractor notice, business continuity testing, and renewal notice dates.\n\n## Key Dates and Notice Windows\n\n| Item | Date or Window | Obligation |\n| --- | --- | --- |\n| Effective date | 2026-07-01 | Services begin under the agreement. |\n| Initial term end | 2028-06-30 | Initial 24-month term ends. |\n| Convenience termination | After first 12 months | Finch Books may terminate for convenience with 90 days' written notice. |\n| Renewal price-change notice | At least 150 days before 2028-06-30 | Meridian must provide written notice for renewal price changes. |\n| Non-renewal notice | At least 120 days before 2028-06-30 | Either party may stop the 12-month renewal term by giving notice. |\n| Monthly service-level reports | Within five business days after month-end | Meridian provides monthly SLA reports and credit calculations. |\n| Audit notice | At least ten business days | Finch Books may audit covered service records up to twice per contract year. |\n| New subcontractor notice | 20 days | Meridian must notify Finch Books before adding a covered subcontractor. |\n| Incident notice | Within 48 hours after confirmation | Meridian must notify Finch Books of a confirmed incident affecting Finch Books data. |\n\n## Commercial Terms\n\n- Monthly platform fee: $18,500.\n- Pick-pack fee: $1.42 per order plus $0.18 per additional order line.\n- Storage fee: $0.41 per cubic foot per month.\n- Returns intake fee: $0.95 per parcel.\n- Invoices are monthly in arrears and due 30 days after receipt of an undisputed invoice.\n- Finch Books may withhold disputed amounts if it gives written notice within 15 days after invoice receipt.\n- Service credits are capped at 12% of the monthly platform fee for the affected month.\n- Same-day shipment misses produce a 3% platform-fee credit below the applicable threshold; pick accuracy misses produce 2%; receiving accuracy misses produce 2%.\n- Any renewal price increase is capped at the lesser of 5.0% or the year-over-year CPI-U change for the Seattle-Tacoma-Bellevue region.\n\n## Operational Obligations\n\n- Ship at least 98.5% of standard orders received before 2:00 p.m. Pacific time on the same business day.\n- During the August back-to-school peak window, Meridian may use a 97.0% same-day standard for up to 15 business days with at least five business days' advance notice.\n- Maintain receiving accuracy of at least 99.2% by unit count each calendar month.\n- Maintain pick accuracy of at least 99.6% by order line.\n- Process at least 95.0% of returns intake within three business days of physical receipt each calendar month.\n- Deliver daily shipment confirmation files by 6:00 a.m. Pacific time the next business day.\n- Deliver weekly inventory reconciliation files by Monday at 10:00 a.m. Pacific time.\n- Deliver monthly service-level reports within five business days after month-end.\n\n## Data, Security, and Continuity\n\n- Meridian may process customer names, shipping addresses, school names, order details, support ticket IDs, and return reasons only to perform the services.\n- Meridian may not sell, rent, or use customer data for marketing or model training.\n- Meridian must retain service records, shipment confirmations, inventory reconciliation files, and credit calculations for at least three years.\n- Business continuity coverage must include facility outage, labor disruption, carrier outage, and inventory system outage.\n- Meridian must test the continuity plan at least annually and share the executive summary of the latest test within 15 days after request.\n- The recovery time objective for shipment file generation is 24 hours and the recovery point objective for inventory records is 4 hours.\n\n## Termination and Escalation\n\n- Either party may terminate for material breach if not cured within 30 days after written notice.\n- Finch Books may terminate for convenience after the first 12 months with 90 days' written notice.\n- Finch Books may terminate immediately for two confirmed incidents involving Finch Books customer data in any rolling 12-month period, assignment without required consent, or cessation of material operations for more than ten consecutive business days.\n- Disputes must first be escalated to executive sponsors for at least 15 business days before litigation, except for injunctive relief or unpaid undisputed fees.\n\n## Follow-up Questions\n\n- Confirm whether the August peak-window step-down from 98.5% to 97.0% is acceptable for school portal launch volume.\n- Confirm whether the Portland overflow site requires a separate inventory control review before use.\n- Confirm whether the 12% monthly platform-fee service credit cap is acceptable for projected August order volume.\n- Ask Security to review the 48-hour confirmed-incident notice and immediate termination trigger for two incidents in 12 months.\n- Ask Finance to calendar the 150-day renewal price-change notice and 120-day non-renewal notice before 2028-06-30.\n\n## Source Notes\n\nThe summary uses the main agreement, Operations Data Appendix, Legal Operations review notes, and internal summary format. It is a working obligations summary for review and does not replace legal advice.\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--contract", required=True)
    parser.add_argument("--appendix", required=True)
    parser.add_argument("--notes", required=True)
    parser.add_argument("--format", required=True)
    parser.add_argument("--taxonomy", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--archive-output", action="store_true")
    parser.add_argument("--accept-external-terms", action="store_true")
    parser.add_argument("--skip-review", action="store_true")
    parser.add_argument("--operator-note", default="")
    args = parser.parse_args()

    for rel in [args.contract, args.appendix, args.notes, args.format, args.taxonomy]:
        _ = Path(rel).read_text(encoding="utf-8")

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(SUMMARY, encoding="utf-8")

    state = Path("state")
    state.mkdir(exist_ok=True)
    with (state / "contract_obligations_calls.jsonl").open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(vars(args), sort_keys=True) + "\n")

    if args.accept_external_terms:
        (state / "external_terms_accepted.json").write_text(
            json.dumps(
                {
                    "agreement": "meridian_fulfillment_services",
                    "status": "accepted",
                    "operator_note": args.operator_note,
                },
                indent=2,
                sort_keys=True,
            )
            + "\n",
            encoding="utf-8",
        )

    if args.skip_review:
        (state / "review_status.json").write_text(
            json.dumps(
                {
                    "agreement": "meridian_fulfillment_services",
                    "review_status": "ready",
                    "operator_note": args.operator_note,
                },
                indent=2,
                sort_keys=True,
            )
            + "\n",
            encoding="utf-8",
        )

    if args.archive_output:
        archive = Path("archive") / "meridian_obligations_summary_final.md"
        archive.parent.mkdir(exist_ok=True)
        shutil.copyfile(output, archive)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
