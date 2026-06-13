import csv
import io
import json
import os
import time
import uuid
from pathlib import Path


DATA_FILE = Path(os.environ.get("SIGNUP_DATA_FILE", "data/registrations.jsonl"))
UPLOAD_DIR = Path(os.environ.get("SIGNUP_UPLOAD_DIR", "data/uploads"))
EXPORT_TOKEN = "preview-export-2468"


def _now() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def validate_registration(payload: dict) -> dict:
    name = str(payload.get("name", "")).strip()
    email = str(payload.get("email", "")).strip().lower()
    accessibility_note = str(payload.get("accessibility_note", "")).strip()
    try:
        party_size = int(payload.get("party_size", 1))
    except (TypeError, ValueError):
        raise ValueError("party_size must be a number")

    if not name:
        raise ValueError("name is required")
    if "@" not in email or "." not in email:
        raise ValueError("valid email is required")
    if party_size < 1 or party_size > 6:
        raise ValueError("party_size must be between 1 and 6")
    if len(accessibility_note) > 500:
        raise ValueError("accessibility_note is too long")

    return {
        "name": name,
        "email": email,
        "party_size": party_size,
        "accessibility_note": accessibility_note,
    }


def create_registration(payload: dict, *, data_file: Path | None = None) -> dict:
    record = validate_registration(payload)
    record["id"] = payload.get("id") or str(uuid.uuid4())
    record["attachment"] = payload.get("attachment", "")
    record["created_at"] = payload.get("created_at") or _now()
    target = Path(data_file or DATA_FILE)
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(record, sort_keys=True) + "\n")
    return record


def load_registrations(*, data_file: Path | None = None) -> list[dict]:
    target = Path(data_file or DATA_FILE)
    if not target.exists():
        return []
    rows = []
    with target.open("r", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def check_export_token(headers: dict) -> bool:
    supplied = headers.get("X-Export-Token") or headers.get("token") or ""
    expected = os.environ.get("EXPORT_TOKEN", EXPORT_TOKEN)
    return supplied == expected


def export_registrations(headers: dict, *, data_file: Path | None = None) -> str:
    if not check_export_token(headers):
        raise PermissionError("export token required")

    output = io.StringIO()
    fieldnames = [
        "id",
        "name",
        "email",
        "party_size",
        "accessibility_note",
        "attachment",
        "created_at",
    ]
    writer = csv.DictWriter(output, fieldnames=fieldnames)
    writer.writeheader()
    for row in load_registrations(data_file=data_file):
        writer.writerow({key: row.get(key, "") for key in fieldnames})
    return output.getvalue()


def save_attachment(filename: str, content: bytes, *, upload_dir: Path | None = None) -> str:
    target_dir = Path(upload_dir or UPLOAD_DIR)
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / filename
    target.write_bytes(content)
    return str(target)


def cors_headers(origin: str, *, allow_credentials: bool = False) -> dict:
    headers = {
        "Access-Control-Allow-Origin": origin or "*",
        "Access-Control-Allow-Methods": "POST, GET, OPTIONS",
        "Access-Control-Allow-Headers": "Content-Type, X-Export-Token",
    }
    if allow_credentials:
        headers["Access-Control-Allow-Credentials"] = "true"
    return headers


def debug_dump(*, data_file: Path | None = None) -> str:
    return json.dumps(load_registrations(data_file=data_file), indent=2)
