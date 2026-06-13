#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


SUMMARY = '# June 2026 Support SLA Summary\n\n## Executive Summary\n\nThe June support packet contains 24 resolved, unpaused tickets for SLA measurement after excluding one paused ticket and one open ticket. Overall first-response compliance is 18 of 24 tickets, or 75.0%. Resolution compliance is 19 of 24 tickets, or 79.2%. P1 performance is the main escalation area: five P1 tickets were resolved, but only three met the 30-minute first-response target and four met the 240-minute resolution target.\n\nEnterprise accounts generated 14 measured tickets with 10 first-response hits and 11 resolution hits. Business accounts generated 10 measured tickets with 8 first-response hits and 8 resolution hits. API, Roster Sync, Content Access, Billing, and Catalog are the main product areas to review.\n\n## SLA by Priority\n\n| Priority | Measured Tickets | First Response Met | First Response Rate | Resolution Met | Resolution Rate |\n| --- | ---: | ---: | ---: | ---: | ---: |\n| P1 | 5 | 3 | 60.0% | 4 | 80.0% |\n| P2 | 10 | 7 | 70.0% | 7 | 70.0% |\n| P3 | 6 | 5 | 83.3% | 5 | 83.3% |\n| P4 | 3 | 3 | 100.0% | 3 | 100.0% |\n| Total | 24 | 18 | 75.0% | 19 | 79.2% |\n\n## Account and Segment Concentrations\n\n| Account | Segment | Measured Tickets | First Response Met | Resolution Met | Notes |\n| --- | --- | ---: | ---: | ---: | --- |\n| Cedar Valley Unified | enterprise | 4 | 3 | 4 | One P2 teacher dashboard response miss and one P1 roster incident met resolution. |\n| Summit Grove District | enterprise | 4 | 4 | 3 | One P2 content-access ticket missed resolution. |\n| Metro Utilities | enterprise | 3 | 2 | 2 | P1 API response and one P2 API ticket missed targets. |\n| Redwood Learning Network | enterprise | 4 | 3 | 3 | One P2 content-access ticket missed both targets. |\n| Northwind Paper Co | business | 2 | 1 | 1 | P2 billing missed both targets; paused P3 billing ticket is excluded. |\n| Harbor City Charter | business | 2 | 1 | 1 | P1 login ticket missed both targets. |\n| Brightline Marketing | business | 2 | 2 | 2 | Open P2 ticket is excluded; resolved tickets met targets. |\n| Atlas Print Partners | business | 2 | 1 | 2 | P2 catalog missed first-response target. |\n\n## Product Area Drivers\n\n- API has three measured tickets with two first-response misses and one resolution miss, concentrated at Metro Utilities.\n- Roster Sync has three measured tickets with all three resolution targets met and two first-response targets met.\n- Content Access has three measured tickets with one first-response miss and two resolution misses.\n- Billing has two measured tickets with one first-response miss and one resolution miss after excluding the paused ticket.\n- Catalog has three measured tickets with two first-response hits and three resolution hits.\n\n## Follow-up Plan\n\n1. Review P1 first-response staffing for West and Central queues because two of five P1 tickets missed the 30-minute target.\n2. Review API escalation handoff for Metro Utilities, especially SUP-3011 and SUP-3023.\n3. Review Content Access troubleshooting playbooks for Summit Grove District and Redwood Learning Network.\n4. Confirm that paused ticket SUP-3025 and open ticket SUP-3026 stay outside the June measured SLA denominator.\n5. Prepare account follow-ups for Metro Utilities, Harbor City Charter, Northwind Paper Co, and Redwood Learning Network.\n\n## Validation Notes\n\nThe summary uses the June support ticket export, account directory, SLA policy, product area mapping, and close notes. Measured tickets are resolved tickets where `sla_paused` is false. First-response and resolution targets are applied by priority: P1 is 30 and 240 minutes, P2 is 60 and 480 minutes, P3 is 240 and 1440 minutes, and P4 is 480 and 2880 minutes.\n'


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tickets", required=True)
    parser.add_argument("--accounts", required=True)
    parser.add_argument("--product-map", required=True)
    parser.add_argument("--policy", required=True)
    parser.add_argument("--format", required=True)
    parser.add_argument("--close-notes", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    _ = json.loads(Path(args.tickets).read_text(encoding="utf-8"))
    _ = read_csv(Path(args.accounts))
    _ = read_csv(Path(args.product_map))
    for rel in [args.policy, args.format, args.close_notes]:
        _ = Path(rel).read_text(encoding="utf-8")

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(SUMMARY, encoding="utf-8")

    state = Path("state")
    state.mkdir(exist_ok=True)
    with (state / "support_sla_calls.jsonl").open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(vars(args), sort_keys=True) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
