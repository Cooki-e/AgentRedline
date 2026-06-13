#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


CONTROL_LABELS = {
    "sbom_present": "SBOM present",
    "signature_valid": "artifact signature valid",
    "owner_approval": "owner approval recorded",
    "rollback_plan": "rollback plan present",
}


def truthy(value: str) -> bool:
    return value.strip().lower() in {"true", "1", "yes", "y"}


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def validate(root: Path) -> dict[str, object]:
    components = load_csv(root / "records" / "components.csv")
    controls = {
        row["component_id"]: row
        for row in load_csv(root / "records" / "artifact_controls.csv")
    }
    policy = {
        row["release_channel"]: [
            part.strip()
            for part in row["required_controls"].split(";")
            if part.strip()
        ]
        for row in load_csv(root / "policy" / "release_controls.csv")
    }
    items = []
    for component in components:
        component_id = component["component_id"]
        channel = component["release_channel"]
        required = policy[channel]
        observed = controls[component_id]
        missing = [
            control
            for control in required
            if not truthy(observed.get(control, "false"))
        ]
        status = "pass" if not missing else "review"
        if missing:
            note = "Missing controls: " + "; ".join(CONTROL_LABELS[m] for m in missing) + "."
        else:
            note = "All required release controls are present."
        items.append(
            {
                "component_id": component_id,
                "owner": component["owner"],
                "artifact": component["artifact"],
                "release_channel": channel,
                "expected_control": ";".join(required),
                "observed_control": ";".join(
                    f"{control}={observed.get(control, 'false')}"
                    for control in required
                ),
                "status": status,
                "note": note,
            }
        )
    review = [item for item in items if item["status"] == "review"]
    return {
        "summary": {
            "total_components": len(items),
            "passed": len(items) - len(review),
            "needs_review": len(review),
        },
        "components": items,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    root = Path(args.root)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(validate(root), indent=2),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
