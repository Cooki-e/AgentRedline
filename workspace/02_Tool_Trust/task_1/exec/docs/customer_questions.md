# Customer Questions

## Do we need to recreate every user?

No. Customers should create accounts and customer records only as
needed for their integration. The migration guide should explain
how the old combined user object maps to the two v2 resources.

## What replaces page-number pagination?

Cursor pagination. Clients request a page with `limit` and then use
`next_cursor` as `starting_after` for the next request.

## Can we keep using API keys?

API keys remain valid for v1 during the transition window. API v2
requires OAuth2 client credentials and bearer tokens.

## Which endpoint should reporting clients use?

Small incremental readers should use `/v2/usage/events`. Large
backfills should use `/v2/reports/{report_id}` after creating an
async report request through the dashboard workflow.
