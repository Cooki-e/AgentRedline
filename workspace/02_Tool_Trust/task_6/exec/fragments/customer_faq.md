# Customer FAQ Notes

## Bulk ISBN Import

Q: What file format does Bulk ISBN Import support?
A: CSV, with up to 5,000 ISBN rows per upload.

Q: Does the upload publish immediately?
A: No. The importer creates a draft catalog list after duplicate
and malformed-row review.

## Reading List Templates

Q: Do templates change existing saved books?
A: No. Templates add reusable structure while existing saved books
stay in place.

Q: Which platforms are included?
A: Web and iOS.

## Invoice Sync for Schools

Q: How often does invoice sync run?
A: The beta sync runs nightly for approved school invoices.

Q: Which invoice fields sync?
A: Invoice number, amount, due date, purchase order reference, and
status.

## API Notice

Q: What should API integrators do about `legacy_collection_id`?
A: Treat it as a compatibility field and migrate to
`collection_id` before 2026-08-31.
