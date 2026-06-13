#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


def truthy(value: str) -> bool:
    return value.strip().lower() in {"true", "1", "yes", "y"}


def load_inventory(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def evaluate(row: dict[str, str], policy: dict[str, object]) -> dict[str, str]:
    reasons = []
    actions = []
    package = row["package"]
    license_name = row["license"]
    scope = row["scope"]
    vuln = row["vuln_severity"].lower()
    network = truthy(row["network_capability"])
    owner_approval = truthy(row["owner_approval"])
    months = int(row["last_release_months"])

    approved_licenses = set(policy["approved_licenses"])
    blocked_runtime = set(policy["blocked_runtime_licenses"])
    review_vulns = set(policy["review_vulnerability_levels"])
    stale_threshold = int(policy["stale_runtime_month_threshold"])

    if scope == "runtime" and license_name in blocked_runtime:
        reasons.append(f"Runtime dependency uses blocked license {license_name}.")
        actions.append("Replace dependency or request legal exception.")
    elif license_name not in approved_licenses:
        reasons.append(f"License {license_name} is not in the approved policy bundle.")
        actions.append("Request license review before release.")

    if vuln in review_vulns:
        reasons.append(f"Vulnerability severity is {vuln}.")
        actions.append("Patch, upgrade, or file security exception.")
    elif vuln == "medium":
        reasons.append("Medium vulnerability allowed with note under current policy.")

    if scope == "runtime" and network and policy["network_capability_requires_owner_approval"] and not owner_approval:
        reasons.append("Runtime dependency has network capability without owner approval.")
        actions.append("Collect owner approval or disable network capability.")

    if scope == "runtime" and months > stale_threshold:
        reasons.append(f"Runtime dependency is stale: last release was {months} months ago.")
        actions.append("Upgrade dependency or document maintenance exception.")

    status = "review" if any(
        phrase not in {"Medium vulnerability allowed with note under current policy."}
        for phrase in reasons
    ) else "pass"
    if not reasons:
        reasons.append("Approved license and no policy review triggers.")
    if not actions:
        actions.append("No follow-up required.")

    return {
        "package": package,
        "version": row["version"],
        "owner": row["owner"],
        "component": row["component"],
        "license": license_name,
        "scope": scope,
        "vuln_severity": row["vuln_severity"],
        "network_capability": row["network_capability"],
        "policy_status": status,
        "reason": " ".join(reasons),
        "recommended_action": " ".join(actions),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--inventory", required=True)
    parser.add_argument("--policy", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    inventory = load_inventory(Path(args.inventory))
    policy = json.loads(Path(args.policy).read_text(encoding="utf-8"))
    dependencies = [evaluate(row, policy) for row in inventory]
    review = [item for item in dependencies if item["policy_status"] == "review"]
    output = {
        "policy_bundle_id": policy.get("bundle_id", "unknown"),
        "summary": {
            "total_dependencies": len(dependencies),
            "passed": len(dependencies) - len(review),
            "needs_review": len(review),
        },
        "dependencies": dependencies,
    }
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(output, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
