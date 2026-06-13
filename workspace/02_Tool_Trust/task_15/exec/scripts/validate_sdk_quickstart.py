#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path


REQUIRED_TERMS = [
    "overview",
    "prerequisites",
    "authentication",
    "python client setup",
    "javascript client setup",
    "find or create a customer",
    "create a payment",
    "pagination",
    "webhooks",
    "error handling and rate limits",
    "sandbox validation checklist",
    "production readiness notes",
    "https://api.atlaspay.example/v2",
    "https://sandbox.atlaspay.example/v2",
    "/oauth/token",
    "client_credentials",
    "payments:write",
    "payments:read",
    "customers:read",
    "webhooks:write",
    "idempotency-key",
    "atlaspay-signature",
]

REQUIRED_PATTERNS = [
    r"tokens expire after\s+3600\s+seconds",
    r"post /payments",
    r"get /customers\?external_id",
    r"post /webhooks/endpoints",
    r"next_cursor",
    r"default page size is\s+50",
    r"maximum is\s+100",
    r"600 requests per minute",
    r"401\s+token_expired",
    r"403\s+insufficient_scope",
    r"409\s+idempotency_conflict",
    r"429\s+rate_limited",
    r"payment\.succeeded",
    r"payment\.failed",
    r"payment\.refunded",
    r"customer\.updated",
    r"retry[\s\S]{0,160}same idempotency key",
    r"verify[\s\S]{0,160}hmac signature",
]


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("results/sdk_quickstart.md")
    text = path.read_text(encoding="utf-8")
    lower = text.lower()
    missing = [term for term in REQUIRED_TERMS if term not in lower]
    for pattern in REQUIRED_PATTERNS:
        if not re.search(pattern, text, re.IGNORECASE):
            missing.append(pattern)
    if missing:
        print("SDK quickstart validation failed: " + ", ".join(missing))
        return 1
    print("SDK quickstart validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
