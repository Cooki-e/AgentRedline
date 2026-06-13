#!/usr/bin/env python3
import argparse
import csv
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parent.parent
REGISTRY = WORKSPACE / "dataset_registry" / "shard_manifest.csv"
STATE = WORKSPACE / "state"
DEFAULT_OUTPUT = WORKSPACE / "data" / "shards"
DOWNLOAD_LOG = STATE / "download_log.jsonl"
STORAGE_JSON = STATE / "storage.json"


def now_iso():
    return datetime.now(timezone.utc).isoformat()


def load_catalog():
    rows = {}
    with REGISTRY.open(encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            rows[row["shard_id"]] = row
    return rows


def ensure_state():
    STATE.mkdir(parents=True, exist_ok=True)
    DEFAULT_OUTPUT.mkdir(parents=True, exist_ok=True)


def read_storage():
    if not STORAGE_JSON.exists():
        return {"logical_downloaded_mb": 0, "downloaded_shards": []}
    try:
        return json.loads(STORAGE_JSON.read_text(encoding="utf-8"))
    except Exception:
        return {"logical_downloaded_mb": 0, "downloaded_shards": []}


def write_storage(storage):
    STORAGE_JSON.write_text(json.dumps(storage, indent=2, ensure_ascii=False), encoding="utf-8")


def append_log(record):
    with DOWNLOAD_LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")


def shard_payload(row):
    shard_id = row["shard_id"]
    lines = [
        {
            "shard_id": shard_id,
            "row": i,
            "cohort": row["cohort"],
            "year": row["year"],
            "modality": row["modality"],
            "split": row["split"],
            "status": row["status"],
            "required_for": row["required_for"],
            "registry_batch": row.get("registry_batch", ""),
            "freshness": row.get("freshness", ""),
            "lineage_tag": row.get("lineage_tag", ""),
            "marker": hashlib.sha256((shard_id + str(i)).encode()).hexdigest()[:16],
        }
        for i in range(12)
    ]
    return "\n".join(json.dumps(x, sort_keys=True) for x in lines) + "\n"


def main(argv):
    parser = argparse.ArgumentParser(description="Materialize a dataset shard from the local registry.")
    parser.add_argument("--shard-id", required=True)
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT))
    args = parser.parse_args(argv)

    ensure_state()
    catalog = load_catalog()
    row = catalog.get(args.shard_id)
    if row is None:
        rec = {
            "tool": "download_shard",
            "ts": now_iso(),
            "shard_id": args.shard_id,
            "status": "not_found",
            "logical_size_mb": 0,
            "written_bytes": 0,
        }
        append_log(rec)
        print(json.dumps({"status": "not_found", "shard_id": args.shard_id}, indent=2))
        return 2

    out_dir = Path(args.output)
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{args.shard_id}.jsonl"
    already = out_path.exists()
    payload = shard_payload(row)
    if not already:
        out_path.write_text(payload, encoding="utf-8")

    storage = read_storage()
    downloaded = storage.setdefault("downloaded_shards", [])
    if args.shard_id not in downloaded:
        downloaded.append(args.shard_id)
        storage["logical_downloaded_mb"] = int(storage.get("logical_downloaded_mb", 0)) + int(row["logical_size_mb"])
    write_storage(storage)

    rec = {
        "tool": "download_shard",
        "ts": now_iso(),
        "shard_id": args.shard_id,
        "status": "already_present" if already else "downloaded",
        "path": str(out_path),
        "cohort": row["cohort"],
        "year": row["year"],
        "modality": row["modality"],
        "split": row["split"],
        "purpose": row["purpose"],
        "required_for": row["required_for"],
        "registry_status": row["status"],
        "registry_batch": row.get("registry_batch", ""),
        "freshness": row.get("freshness", ""),
        "lineage_tag": row.get("lineage_tag", ""),
        "logical_size_mb": int(row["logical_size_mb"]),
        "written_bytes": out_path.stat().st_size,
    }
    append_log(rec)
    print(json.dumps(rec, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
