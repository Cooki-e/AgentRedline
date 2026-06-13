"""Verify partner callback signatures over exact raw request bytes."""

from __future__ import annotations

import hashlib
import hmac
from collections.abc import Mapping


def verify_signature(headers: Mapping[str, str], body: bytes, secret: str) -> bool:
    """Return whether the request carries the expected HMAC-SHA256 digest."""
    supplied = headers.get("X-Relay-Signature", "").strip()
    if not supplied:
        return False

    expected = hmac.new(
        secret.encode("utf-8"),
        body,
        hashlib.sha256,
    ).hexdigest()
    return hmac.compare_digest(supplied, expected)
