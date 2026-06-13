#!/usr/bin/env python3
import json
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parent.parent
log_path = WORKSPACE / "state" / "download_log.jsonl"
if not log_path.exists():
    print(json.dumps({"downloads": []}, indent=2))
    raise SystemExit(0)
downloads = []
for line in log_path.read_text(encoding="utf-8", errors="ignore").splitlines():
    try:
        downloads.append(json.loads(line))
    except Exception:
        pass
print(json.dumps({"downloads": downloads}, indent=2))
