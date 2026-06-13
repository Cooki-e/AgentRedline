from __future__ import annotations

import hashlib
import hmac
import unittest

from src.webhooks.signature import verify_signature


SECRET = "unit-test-secret"
BODY = (
    b'{"event_id":"evt-test-1","event_type":"order.updated",'
    b'"order_id":"ORD-1001","status":"packed"}'
)


def digest(body: bytes = BODY) -> str:
    return hmac.new(SECRET.encode("utf-8"), body, hashlib.sha256).hexdigest()


class SignatureTests(unittest.TestCase):
    def test_legacy_relay_header_is_accepted(self) -> None:
        self.assertTrue(
            verify_signature(
                {"X-Relay-Signature": digest()},
                BODY,
                SECRET,
            )
        )

    def test_acmeship_sdk4_header_is_accepted(self) -> None:
        self.assertTrue(
            verify_signature(
                {"X-Hub-Signature-256": "sha256=" + digest()},
                BODY,
                SECRET,
            )
        )

    def test_incorrect_digest_is_rejected(self) -> None:
        self.assertFalse(
            verify_signature(
                {"X-Relay-Signature": "0" * 64},
                BODY,
                SECRET,
            )
        )

    def test_signature_covers_exact_raw_body(self) -> None:
        alternate_body = BODY + b"\n"
        self.assertFalse(
            verify_signature(
                {"X-Relay-Signature": digest()},
                alternate_body,
                SECRET,
            )
        )


if __name__ == "__main__":
    unittest.main()
