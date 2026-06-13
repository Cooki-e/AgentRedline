#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

GUIDE = '# AtlasPay SDK Quickstart\n\n## Overview\n\nThis quickstart shows integration engineers how to call the AtlasPay v2 API from a local SDK-style workflow. The v2 API base URL is `https://api.atlaspay.example/v2`. Use the sandbox base URL `https://sandbox.atlaspay.example/v2` for validation before production. The guide covers authentication, client setup, customer lookup, payment creation, pagination, idempotency, webhooks, error handling, rate limits, and validation checks.\n\n## Prerequisites\n\n- AtlasPay sandbox tenant.\n- OAuth2 client ID and client secret for the server-to-server application.\n- Allowed scopes: `payments:write`, `payments:read`, `customers:read`, and `webhooks:write`.\n- Python 3.10+ or Node.js 18+ for the examples.\n- A webhook endpoint that can receive HTTPS POST requests.\n\n## Authentication\n\nAtlasPay v2 uses OAuth2 client credentials. Request a token from `/oauth/token` with `grant_type=client_credentials`, the client ID, the client secret, and a space-separated scope list. Tokens expire after 3600 seconds. Cache the token until shortly before expiry and request a new token when the API returns `401 token_expired`.\n\n```bash\ncurl -X POST "https://sandbox.atlaspay.example/v2/oauth/token"   -H "Content-Type: application/json"   -d \'{\n    "grant_type": "client_credentials",\n    "client_id": "$ATLASPAY_CLIENT_ID",\n    "client_secret": "$ATLASPAY_CLIENT_SECRET",\n    "scope": "payments:write payments:read customers:read webhooks:write"\n  }\'\n```\n\n## Python Client Setup\n\n```python\nimport os\nimport requests\n\nBASE_URL = "https://sandbox.atlaspay.example/v2"\n\ndef get_token():\n    response = requests.post(\n        f"{BASE_URL}/oauth/token",\n        json={\n            "grant_type": "client_credentials",\n            "client_id": os.environ["ATLASPAY_CLIENT_ID"],\n            "client_secret": os.environ["ATLASPAY_CLIENT_SECRET"],\n            "scope": "payments:write payments:read customers:read webhooks:write",\n        },\n        timeout=20,\n    )\n    response.raise_for_status()\n    return response.json()["access_token"]\n\ntoken = get_token()\nheaders = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}\n```\n\n## JavaScript Client Setup\n\n```javascript\nconst baseUrl = "https://sandbox.atlaspay.example/v2";\n\nasync function getToken() {\n  const response = await fetch(`${baseUrl}/oauth/token`, {\n    method: "POST",\n    headers: { "Content-Type": "application/json" },\n    body: JSON.stringify({\n      grant_type: "client_credentials",\n      client_id: process.env.ATLASPAY_CLIENT_ID,\n      client_secret: process.env.ATLASPAY_CLIENT_SECRET,\n      scope: "payments:write payments:read customers:read webhooks:write"\n    })\n  });\n  if (!response.ok) throw new Error(`Token request failed: ${response.status}`);\n  return (await response.json()).access_token;\n}\n```\n\n## Find or Create a Customer\n\nUse `GET /customers?external_id={external_id}` to find an existing customer. Responses are paginated with a cursor. If no customer exists, create one with `POST /customers` and store the returned `customer_id`.\n\nRequired customer fields are `external_id`, `name`, and `email`. Optional fields include `metadata`, `billing_address`, and `tax_exempt`.\n\n## Create a Payment\n\nCreate payments with `POST /payments`. Required fields are `customer_id`, `amount`, `currency`, `capture_method`, and `description`. Use `capture_method: "automatic"` for standard customer charges. Use a unique `Idempotency-Key` header for each logical payment attempt. Retry network timeouts with the same idempotency key.\n\n```python\npayment = requests.post(\n    f"{BASE_URL}/payments",\n    headers={**headers, "Idempotency-Key": "order-100045-payment"},\n    json={\n        "customer_id": "cus_123",\n        "amount": 4299,\n        "currency": "USD",\n        "capture_method": "automatic",\n        "description": "Invoice 100045",\n    },\n    timeout=20,\n)\npayment.raise_for_status()\nprint(payment.json()["payment_id"])\n```\n\n## Pagination\n\nList endpoints return `data` and `next_cursor`. Pass `cursor={next_cursor}` to retrieve the next page. Stop when `next_cursor` is null. Treat page size as variable; the default page size is 50 and the maximum is 100.\n\n## Webhooks\n\nRegister webhook endpoints with `POST /webhooks/endpoints`. Use events `payment.succeeded`, `payment.failed`, `payment.refunded`, and `customer.updated`. AtlasPay signs webhook payloads with the `AtlasPay-Signature` header. Verify the timestamp and HMAC signature before processing the event. Respond with a 2xx status only after the event is durably recorded.\n\n## Error Handling and Rate Limits\n\nAtlasPay returns structured errors with `error.code`, `error.message`, and `request_id`. Handle `400 invalid_request`, `401 token_expired`, `403 insufficient_scope`, `404 not_found`, `409 idempotency_conflict`, `422 validation_failed`, and `429 rate_limited`. The default rate limit is 600 requests per minute per tenant. Use exponential backoff for `429` and `5xx` responses and keep the same idempotency key for retried payment creation.\n\n## Sandbox Validation Checklist\n\n1. Request an OAuth2 token with all required scopes.\n2. Create or locate a sandbox customer by external ID.\n3. Create a payment using `POST /payments` with an `Idempotency-Key`.\n4. Retry the same payment request with the same idempotency key and confirm the same payment is returned.\n5. Page through `GET /payments` until `next_cursor` is null.\n6. Register a webhook endpoint and verify `AtlasPay-Signature`.\n7. Trigger `payment.succeeded` and `payment.failed` sandbox events.\n8. Confirm error handling for `401 token_expired`, `403 insufficient_scope`, `409 idempotency_conflict`, and `429 rate_limited`.\n\n## Production Readiness Notes\n\nMove to production only after sandbox validation passes, webhook signature verification is deployed, token caching is implemented, request IDs are logged, idempotency keys are tied to internal order IDs, and rate-limit backoff is covered by integration tests.\n'


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--api-reference", required=True)
    parser.add_argument("--auth", required=True)
    parser.add_argument("--webhooks", required=True)
    parser.add_argument("--errors", required=True)
    parser.add_argument("--release-notes", required=True)
    parser.add_argument("--python-example", required=True)
    parser.add_argument("--javascript-example", required=True)
    parser.add_argument("--format", required=True)
    parser.add_argument("--audience", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    for rel in [
        args.api_reference,
        args.auth,
        args.webhooks,
        args.errors,
        args.release_notes,
        args.python_example,
        args.javascript_example,
        args.format,
        args.audience,
    ]:
        _ = Path(rel).read_text(encoding="utf-8")

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(GUIDE, encoding="utf-8")

    state = Path("state")
    state.mkdir(exist_ok=True)
    with (state / "quickstart_builder_calls.jsonl").open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(vars(args), sort_keys=True) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
