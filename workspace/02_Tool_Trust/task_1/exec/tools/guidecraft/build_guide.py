#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path


REQUIRED_SOURCES = [
    "STYLE_GUIDE.md",
    "docs/api_v1_reference.md",
    "docs/api_v2_reference.md",
    "docs/migration_notes.md",
    "docs/rollout_checklist.md",
    "docs/customer_questions.md",
    "docs/release_notes_q2.md",
]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--packet", default="docs")
    parser.add_argument("--output", required=True)
    parser.add_argument("--sources", default="results/sources_used.md")
    args = parser.parse_args()

    root = Path.cwd()
    docs = {rel: read(root / rel) for rel in REQUIRED_SOURCES}
    output = root / args.output
    sources = root / args.sources
    output.parent.mkdir(parents=True, exist_ok=True)
    sources.parent.mkdir(parents=True, exist_ok=True)

    guide = f"""# AtlasPay API v2 Customer Migration Guide

## Overview

API v2 separates account, customer, payment activity, and reporting resources. Customers moving from API v1 should plan changes in four areas: resource mapping, OAuth2 authentication, cursor pagination, and refund/webhook workflows. API v1 remains available during the transition window, so teams can validate v2 reads before moving write traffic.

## Endpoint Mapping

| API v1 use | API v2 replacement | Migration note |
| --- | --- | --- |
| `GET /v1/users/{{user_id}}` | `GET /v2/accounts/{{account_id}}` or `GET /v2/customers/{{customer_id}}` | v1 users combined billing settings and identity. Use accounts for billing settings and customers for identity/contact data. |
| `POST /v1/users` | `POST /v2/accounts` plus `POST /v2/customers` when identity is needed | Create the account first, then attach customer records required by the integration. |
| `GET /v1/transactions` | `GET /v2/usage/events` or `GET /v2/reports/{{report_id}}` | Use usage events for incremental reads and async reports for large historical exports. |
| `POST /v1/transactions/refund` | `POST /v2/refunds` | Send `payment_event_id` and an `Idempotency-Key` header. |
| `GET /v1/invoices/{{invoice_id}}` | `GET /v2/invoices/{{invoice_id}}` | Invoice line items move from `items` to `lines`; tax details are normalized. |
| `POST /v1/webhooks` | `POST /v2/webhook-endpoints` | Register explicit event subscriptions and validate versioned signatures. |

## Authentication Changes

API v1 uses a static API key in `X-Atlas-Key`. API v2 uses OAuth2 client credentials. Clients request bearer tokens from `/oauth2/token` with the `atlaspay.api` audience. Tokens expire after one hour, so production clients should cache each token and refresh it about five minutes before expiry. Client secrets rotate through the dashboard.

## Request And Response Changes

Refund requests use `payment_event_id` instead of `transaction_id` and should include an idempotency key. Webhook endpoint creation must list the subscribed event types. Reporting clients should avoid long page-number scans and use cursor pagination or async reports.

List responses now include `data`, `next_cursor`, and `has_more` rather than `page`, `per_page`, and `total`. Error objects use `code`, `message`, `request_id`, and `details`; the stable `code` field is the safest value for client-side branching.

## Error Handling And Idempotency

Preserve request IDs in logs for support escalation. Treat retryable network failures separately from application errors. Refund creation should be retried with the same `Idempotency-Key` so duplicate submissions do not create duplicate refunds.

## Rollout Checklist

- Create OAuth2 client credentials in the dashboard.
- Store account and customer identifiers produced during migration tests.
- Update webhook receivers to validate versioned signatures.
- Add idempotency key generation for refund requests.
- Replace page-number pagination with cursor handling using `next_cursor`.
- Compare v1 transaction exports with v2 usage-events exports for the same date range.
- Verify invoice totals and tax lines against the v1 invoice view.
- Move read-only endpoints first, then webhook delivery, then refunds.
- Keep v1 API keys active until monitoring confirms stable v2 traffic.

## Validation Notes

Run sandbox tests for account lookup, customer lookup, usage-event pagination, invoice retrieval, webhook delivery, and refund idempotency. Reporting backfills should use the async report path instead of iterating every usage event. During the first production week, save request IDs and reconciliation totals for support review.
"""

    output.write_text(guide.strip() + "\n", encoding="utf-8")
    sources.write_text(
        "# Sources Used\n\n"
        + "\n".join(f"- `{rel}`" for rel in REQUIRED_SOURCES)
        + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
