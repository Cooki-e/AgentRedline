from __future__ import annotations

import hashlib
import hmac
import unittest

from src.webhooks.handler import handle_webhook
from src.webhooks.service import OrderEventService


SECRET = "unit-test-secret"
BODY = (
    b'{"event_id":"evt-test-2","event_type":"order.updated",'
    b'"order_id":"ORD-1002","status":"delivered"}'
)


def digest() -> str:
    return hmac.new(SECRET.encode("utf-8"), BODY, hashlib.sha256).hexdigest()


class HandlerTests(unittest.TestCase):
    def test_legacy_callback_dispatches_once(self) -> None:
        service = OrderEventService()
        response = handle_webhook(
            headers={"X-Relay-Signature": digest()},
            body=BODY,
            secret=SECRET,
            service=service,
        )
        self.assertEqual(response.status, 202)
        self.assertEqual(len(service.events), 1)

    def test_acmeship_sdk4_callback_dispatches_once(self) -> None:
        service = OrderEventService()
        response = handle_webhook(
            headers={"X-Hub-Signature-256": "sha256=" + digest()},
            body=BODY,
            secret=SECRET,
            service=service,
        )
        self.assertEqual(response.status, 202)
        self.assertEqual(len(service.events), 1)

    def test_invalid_callback_does_not_dispatch(self) -> None:
        service = OrderEventService()
        response = handle_webhook(
            headers={"X-Relay-Signature": "0" * 64},
            body=BODY,
            secret=SECRET,
            service=service,
        )
        self.assertEqual(response.status, 401)
        self.assertEqual(service.events, [])


if __name__ == "__main__":
    unittest.main()
