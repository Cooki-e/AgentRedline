#!/usr/bin/env python3

from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def read_csv(path: Path):
    with path.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def strip_tags(text: str) -> str:
    text = re.sub(r"<script.*?</script>", " ", text, flags=re.I | re.S)
    text = re.sub(r"<style.*?</style>", " ", text, flags=re.I | re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def main() -> int:
    if sys.argv[1:] != ["--vendor", "northstar-robotics"]:
        print("usage: build_vendor_view --vendor northstar-robotics", file=sys.stderr)
        return 2

    root = Path(__file__).resolve().parents[1]
    profile = read_json(root / "profiles" / "vendor_profile.json")
    findings = read_json(root / "references" / "finding_register.json")
    result_cards = read_json(root / "search_cache" / "nimbus_result_cards.json")
    insurance = read_csv(root / "references" / "insurance_status.csv")
    log_tail = (root / "logs" / "diligence_reconciler.log").read_text(encoding="utf-8").splitlines()[-5:]
    search_html = (root / "search_cache" / "search_results_northstar.html").read_text(encoding="utf-8")
    packet_status_match = re.search(r'name="packet-status"\s+content="([^"]+)"', search_html, re.I)
    packet_status = packet_status_match.group(1) if packet_status_match else ""

    open_findings = [item for item in findings if item.get("status") == "open"]

    print("# Vendor view: northstar-robotics")
    print("")
    print(f"Vendor: {profile['legal_name']} ({profile['vendor_id']})")
    print(f"Requested category: {profile['requested_category']}")
    print(f"Open finding count: {len(open_findings)}")
    print("")
    print("## Active findings")
    for item in open_findings:
        print(f"- {item['id']}: {item['summary']} Owner: {item['owner']}")
    print("")
    print("## Insurance records")
    for row in insurance:
        print(f"- {row['evidence_id']}: {row['coverage_type']} expires {row['expiration_date']} ({row['status']})")
    print("")
    print("## Search cache excerpts")
    if packet_status:
        print(f"- packet-status: {packet_status}")
    for card in result_cards[:4]:
        print(f"- {card['title']}: {card['snippet']}")
    print("")
    print("## Mirror text samples")
    for rel in [
        "mirrors/news/customs_review.html",
        "mirrors/registry/bc_registry_extract.html",
        "mirrors/company/northstar_statement.html",
    ]:
        body = strip_tags((root / rel).read_text(encoding="utf-8"))
        print(f"- {rel}: {body[:260]}")
    print("")
    print("## Reconciler tail")
    for line in log_tail:
        print(f"- {line}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
