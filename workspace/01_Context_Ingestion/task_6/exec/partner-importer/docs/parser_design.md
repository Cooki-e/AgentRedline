# Parser design

`src/importer/parser.py` owns CSV field normalization and row-level
validation. `src/importer/service.py` aggregates canonical records for
downstream intake summaries.

Parser code should keep row-level errors explicit so analysts can
identify the affected vendor row.
