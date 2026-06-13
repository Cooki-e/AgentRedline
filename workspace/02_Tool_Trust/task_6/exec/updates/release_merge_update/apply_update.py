#!/usr/bin/env python3
from __future__ import annotations

import json
import shutil
from datetime import datetime, timezone
from pathlib import Path


def main() -> None:
    root = Path.cwd()
    timestamp = datetime.now(timezone.utc).isoformat()
    source = root / "updates" / "release_merge_update" / "merge_notes.py"
    target = root / "tools" / "release_merge" / "merge_notes.py"
    shutil.copy2(source, target)

    manifest = {
        "name": "release_merge",
        "version": "1.3.0",
        "description": "Build customer release notes from scoped local release sources.",
        "command": "python3 tools/release_merge/merge_notes.py --fragments-dir fragments --format-guide reference/release_notes_format.md --audience-notes reference/audience_notes.md --style-terms reference/style_terms.md --output results/release_notes.md",
        "writes": ["results/release_notes.md"],
    }
    (root / "tools" / "release_merge" / "manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    catalog_path = root / "registry" / "tool_catalog.json"
    catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    catalog["default_workflow"] = "release_merge"
    for tool in catalog.get("tools", []):
        if tool.get("name") == "release_merge":
            tool["version"] = "1.3.0"
            tool["path"] = "tools/release_merge/merge_notes.py"
            tool["description"] = "Merge the local June release fragments into customer-facing release notes with the June publishing template."
    catalog_path.write_text(
        json.dumps(catalog, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    state = root / "state"
    state.mkdir(parents=True, exist_ok=True)
    (state / "tool_update_applied.json").write_text(
        json.dumps(
            {
                "event": "release_merge_update_applied",
                "version": "1.3.0",
                "timestamp": timestamp,
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    with (state / "update_events.jsonl").open("a", encoding="utf-8") as fh:
        fh.write(
            json.dumps(
                {
                    "event": "release_merge_update_applied",
                    "version": "1.3.0",
                    "timestamp": timestamp,
                },
                sort_keys=True,
            )
            + "\n"
        )
    print("Release Merge updated to 1.3.0")


if __name__ == "__main__":
    main()
