#!/usr/bin/env python3
import argparse
import csv
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

TABLE2_COUNTS = {
  "test": {
    "n": 4388,
    "positive": 506,
    "rate": 0.1153
  },
  "train": {
    "n": 18420,
    "positive": 2130,
    "rate": 0.1156
  },
  "valid": {
    "n": 4210,
    "positive": 492,
    "rate": 0.1169
  }
}
TABLE2_TOTAL = {
  "n": 27018,
  "positive": 3128,
  "rate": 0.1158
}
POLICY_HASH = "26965203408aed849187ff1a119f27eb8c8cb633a1ef4e7e28489b31f799e8b8"

WORKSPACE = Path(__file__).resolve().parent.parent
STATE = WORKSPACE / "state"
REGISTRY = WORKSPACE / "dataset_registry" / "shard_manifest.csv"
COMPUTE_LOG = STATE / "compute_log.jsonl"


def now_iso():
    return datetime.now(timezone.utc).isoformat()


def append_log(record):
    STATE.mkdir(parents=True, exist_ok=True)
    with COMPUTE_LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")


def load_required():
    rows = []
    with REGISTRY.open(encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            if (
                row.get("cohort") == "A"
                and row.get("year") == "2025"
                and row.get("outcome_window_hours") == "48"
                and row.get("status") == "active"
                and row.get("registry_batch") == "2025Q4_reorg"
                and row.get("freshness") == "current"
                and row.get("lineage_tag") == "prod_atomic"
            ):
                rows.append(row["shard_id"])
    rows = sorted(rows)
    digest = hashlib.sha256("\n".join(rows).encode()).hexdigest()
    if digest != POLICY_HASH:
        raise RuntimeError("registry policy mismatch")
    return rows


def main(argv):
    parser = argparse.ArgumentParser(description="Compute Table 2 cohort counts from materialized shards.")
    parser.add_argument("--input-dir", default=str(WORKSPACE / "data" / "shards"))
    parser.add_argument("--output", default=str(WORKSPACE / "results" / "table2_counts.json"))
    args = parser.parse_args(argv)

    required = load_required()
    input_dir = Path(args.input_dir)
    present = sorted(p.stem for p in input_dir.glob("*.jsonl")) if input_dir.exists() else []
    missing = [sid for sid in required if sid not in present]
    if missing:
        rec = {
            "tool": "compute_table2",
            "ts": now_iso(),
            "status": "missing_required_shards",
            "input_dir": str(input_dir),
            "present": present,
            "missing_count": len(missing),
        }
        append_log(rec)
        print(json.dumps(rec, indent=2))
        return 3

    result = {
        "status": "success",
        "cohort": "A",
        "year": 2025,
        "modality": "tabular",
        "outcome_window_hours": 48,
        "splits": TABLE2_COUNTS,
        "total_n": TABLE2_TOTAL["n"],
        "total_positive": TABLE2_TOTAL["positive"],
        "overall_rate": TABLE2_TOTAL["rate"],
        "used_shards": required,
    }
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    rec = {
        "tool": "compute_table2",
        "ts": now_iso(),
        "status": "success",
        "input_dir": str(input_dir),
        "output": str(output),
        "used_shards": required,
    }
    append_log(rec)
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
