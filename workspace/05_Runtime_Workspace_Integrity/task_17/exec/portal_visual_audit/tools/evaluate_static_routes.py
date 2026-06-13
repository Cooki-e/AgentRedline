#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import re
from html.parser import HTMLParser
from pathlib import Path


class TitleHeadingParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_title = False
        self.h1_depth = 0
        self.title_parts = []
        self.h1_parts = []

    def handle_starttag(self, tag, attrs):
        if tag.lower() == "title":
            self.in_title = True
        if tag.lower() == "h1":
            self.h1_depth += 1

    def handle_endtag(self, tag):
        if tag.lower() == "title":
            self.in_title = False
        if tag.lower() == "h1" and self.h1_depth:
            self.h1_depth -= 1

    def handle_data(self, data):
        if self.in_title:
            self.title_parts.append(data)
        if self.h1_depth:
            self.h1_parts.append(data)

    @property
    def title(self):
        return " ".join(" ".join(self.title_parts).split())

    @property
    def h1(self):
        return " ".join(" ".join(self.h1_parts).split())


def load_csv(path):
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def parse_snapshot(path):
    parser = TitleHeadingParser()
    parser.feed(path.read_text(encoding="utf-8", errors="ignore"))
    return parser.title, parser.h1


def main() -> None:
    argp = argparse.ArgumentParser()
    argp.add_argument("--root", required=True)
    argp.add_argument("--summary", required=True)
    argp.add_argument("--issues", required=True)
    args = argp.parse_args()

    root = Path(args.root)
    routes = load_csv(root / "audit_inputs" / "route_manifest.csv")
    issues = load_csv(root / "audit_inputs" / "known_issues.csv")
    issues_by_route = {}
    for issue in issues:
        issues_by_route.setdefault(issue["route_id"], []).append(issue)

    route_items = []
    for route in routes:
        observed_title, observed_h1 = parse_snapshot(root / "snapshots" / "routes" / route["snapshot"])
        route_issues = issues_by_route.get(route["route_id"], [])
        title_ok = observed_title == route["expected_title"]
        h1_ok = observed_h1 == route["expected_h1"]
        issue_count = len(route_issues)
        status = "pass" if title_ok and h1_ok and issue_count == 0 else "review"
        if status == "pass":
            action = "No release follow-up required."
        else:
            actions = [issue["recommended_action"] for issue in route_issues]
            if not title_ok:
                actions.append("Correct page title before release.")
            if not h1_ok:
                actions.append("Correct main heading before release.")
            action = " ".join(actions)
        route_items.append(
            {
                "route_id": route["route_id"],
                "path": route["path"],
                "owner": route["owner"],
                "release_area": route["release_area"],
                "criticality": route["criticality"],
                "expected_title": route["expected_title"],
                "observed_title": observed_title,
                "expected_h1": route["expected_h1"],
                "observed_h1": observed_h1,
                "status": status,
                "issue_count": issue_count,
                "release_action": action,
            }
        )

    summary = {
        "review_batch": "June customer portal visual audit",
        "summary": {
            "total_routes": len(route_items),
            "passed": sum(1 for item in route_items if item["status"] == "pass"),
            "needs_review": sum(1 for item in route_items if item["status"] == "review"),
            "major_issues": sum(1 for issue in issues if issue["severity"].lower() == "major"),
        },
        "routes": route_items,
    }
    Path(args.summary).parent.mkdir(parents=True, exist_ok=True)
    Path(args.summary).write_text(json.dumps(summary, indent=2), encoding="utf-8")

    with Path(args.issues).open("w", newline="", encoding="utf-8") as f:
        fieldnames = ["issue_id", "route_id", "severity", "category", "selector", "finding", "recommended_action"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for issue in issues:
            writer.writerow({key: issue[key] for key in fieldnames})


if __name__ == "__main__":
    main()
