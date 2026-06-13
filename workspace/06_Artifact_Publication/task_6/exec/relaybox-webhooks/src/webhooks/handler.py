"""HTTP-facing partner callback adapter."""

from __future__ import annotations

import json
from collections.abc import Mapping
from typing import Any, Protocol

from .models import Response
from .signature import verify_signature


class EventService(Protocol):
    def process(self, payload: dict[str, Any]) -> None:
        ...


def handle_webhook(
    *,
    headers: Mapping[str, str],
    body: bytes,
    secret: str,
    service: EventService,
) -> Response:
    """Validate, decode, and dispatch one partner callback."""
    if not verify_signature(headers, body, secret):
        return Response(status=401, body={"error": "invalid_signature"})

    try:
        payload = json.loads(body.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        return Response(status=400, body={"error": "invalid_json"})

    service.process(payload)
    return Response(status=202, body={"status": "accepted"})
