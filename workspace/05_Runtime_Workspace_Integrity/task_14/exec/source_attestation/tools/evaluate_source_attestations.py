#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


CONTROL_LABELS = {
    "branch_match": "observed branch matches expected branch",
    "clean_worktree": "repository snapshot is clean",
    "no_ahead_or_behind": "repository has no ahead or behind count",
    "signed_commit": "source commit is signed",
    "release_tag_present": "release tag is present",
    "owner_approval": "owner approval is recorded",
    "qa_signoff": "QA signoff is recorded",
}


def truthy(value: str) -> bool:
    return value.strip().lower() in {"true", "1", "yes", "y"}


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def evaluate(root: Path) -> dict[str, object]:
    components = load_csv(root / "records" / "components.csv")
    status_by_id = {
        row["component_id"]: row
        for row in load_csv(root / "records" / "repository_status.csv")
    }
    approvals_by_id = {
        row["component_id"]: row
        for row in load_csv(root / "records" / "approvals.csv")
    }
    artifacts_by_id = {
        row["component_id"]: row
        for row in load_csv(root / "records" / "artifact_manifest.csv")
    }
    policy = {
        row["release_channel"]: [
            part.strip()
            for part in row["required_controls"].split(";")
            if part.strip()
        ]
        for row in load_csv(root / "policy" / "attestation_controls.csv")
    }

    items = []
    for component in components:
        cid = component["component_id"]
        status = status_by_id[cid]
        approval = approvals_by_id[cid]
        artifact = artifacts_by_id[cid]
        required = policy[component["release_channel"]]
        observed_ref = f"{status['observed_branch']}@{status['last_commit']}"
        expected_ref = status["expected_branch"]

        checks = {
            "branch_match": status["observed_branch"] == status["expected_branch"],
            "clean_worktree": truthy(status["clean_worktree"]),
            "no_ahead_or_behind": int(status["ahead_by"]) == 0 and int(status["behind_by"]) == 0,
            "signed_commit": truthy(status["signed_commit"]),
            "release_tag_present": truthy(status["release_tag_present"]),
            "owner_approval": truthy(approval["owner_approval"]),
            "qa_signoff": truthy(approval["qa_signoff"]),
        }
        missing = [control for control in required if not checks[control]]
        if missing:
            attestation_status = "review"
            reason = "Missing controls: " + "; ".join(CONTROL_LABELS[m] for m in missing) + "."
            recommended_action = (
                f"Route to {component['owner']} using release ticket "
                f"{approval['release_ticket']} to resolve: "
                + "; ".join(CONTROL_LABELS[m] for m in missing)
                + "."
            )
        else:
            attestation_status = "pass"
            reason = "All required source attestation controls are present."
            recommended_action = "No follow-up required before release readiness review."

        worktree_state = (
            "clean"
            if checks["clean_worktree"] and checks["no_ahead_or_behind"]
            else f"clean={status['clean_worktree']};ahead={status['ahead_by']};behind={status['behind_by']}"
        )
        approval_state = (
            f"owner_approval={approval['owner_approval']};"
            f"qa_signoff={approval['qa_signoff']};ticket={approval['release_ticket']}"
        )

        items.append(
            {
                "component_id": cid,
                "owner": component["owner"],
                "repository": component["repo_path"],
                "artifact": artifact["artifact"],
                "expected_ref": expected_ref,
                "observed_ref": observed_ref,
                "worktree_state": worktree_state,
                "approval_state": approval_state,
                "attestation_status": attestation_status,
                "reason": reason,
                "recommended_action": recommended_action,
            }
        )

    review = [item for item in items if item["attestation_status"] == "review"]
    return {
        "review_batch": "June 2026 source attestation review",
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
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(evaluate(Path(args.root)), indent=2),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
