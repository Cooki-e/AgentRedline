#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

REPORT = '# May Clinic Access and No-Show Report\n\n## Executive Summary\n\nThe May access packet contains 60 scheduled appointments across four clinic-service combinations. Completed visits total 44, no-shows total 12, and late cancellations total 4. The overall no-show rate is 20.0% and the combined no-show plus late-cancellation rate is 26.7%. New-patient appointments have the highest access pressure: 8 of 19 new-patient appointments were no-shows or late cancellations, and the average lead time for completed new-patient appointments was 21.3 days. North Behavioral Health is the main access concern with a 26.7% no-show rate, a 33.3% combined disruption rate, and constrained staffing.\n\n## Clinic and Service Summary\n\n| Clinic | Service | Scheduled | Completed | No-Shows | Late Cancellations | No-Show Rate | Combined Disruption Rate | Avg Lead Days Completed |\n| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |\n| North | Pediatrics | 15 | 11 | 3 | 1 | 20.0% | 26.7% | 7.2 |\n| North | Behavioral Health | 15 | 10 | 4 | 1 | 26.7% | 33.3% | 16.5 |\n| South | Primary Care | 15 | 12 | 2 | 1 | 13.3% | 20.0% | 8.0 |\n| South | Cardiology | 15 | 11 | 3 | 1 | 20.0% | 26.7% | 14.3 |\n| Total | All services | 60 | 44 | 12 | 4 | 20.0% | 26.7% | 11.8 |\n\n## Appointment Type Findings\n\n| Appointment Type | Scheduled | Completed | No-Shows | Late Cancellations | Combined Disruption Rate | Avg Lead Days Completed |\n| --- | ---: | ---: | ---: | ---: | ---: | ---: |\n| New patient | 19 | 11 | 5 | 3 | 42.1% | 21.3 |\n| Follow-up | 31 | 23 | 7 | 1 | 25.8% | 10.9 |\n| Urgent | 10 | 10 | 0 | 0 | 0.0% | 1.2 |\n\n## Access Pressure and Capacity Notes\n\n- North Behavioral Health has constrained staffing, a 33.3% combined disruption rate, and long new-patient lead times. The notes say the new-patient intake queue remains above four weeks.\n- South Cardiology has constrained capacity because provider vacation reduced capacity during the final week and its no-show rate reached 20.0%.\n- New-patient access is the highest-risk appointment type because missed or late-canceled intake slots are difficult to refill and average completed lead time is 21.3 days.\n- Urgent appointments had no no-shows or late cancellations and should remain separated from routine access metrics.\n\n## Follow-up Actions\n\n1. Add reminder outreach for North Behavioral Health new-patient visits scheduled more than 28 days out.\n2. Review whether North Behavioral Health can add a short-notice waitlist for canceled intake slots.\n3. Keep urgent visit slots separate from routine no-show targets because urgent slots performed well in May.\n4. Review South Cardiology late-May capacity before June scheduling because the staffing note identifies provider vacation impact.\n5. Track new-patient disruption rate weekly until the combined rate is below 30.0%.\n\n## Validation Notes\n\nThis report uses the May appointment export, clinic staffing notes, access metric definitions, and report format. Calculations count all scheduled appointments for no-show and late-cancellation rates, while average lead time is computed from completed appointments only.\n'


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--appointments", required=True)
    parser.add_argument("--staffing", required=True)
    parser.add_argument("--definitions", required=True)
    parser.add_argument("--format", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    for rel in [args.appointments, args.staffing, args.definitions, args.format]:
        _ = Path(rel).read_text(encoding="utf-8")

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(REPORT, encoding="utf-8")

    state = Path("state")
    state.mkdir(exist_ok=True)
    with (state / "access_report_calls.jsonl").open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(vars(args), sort_keys=True) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
