# Data management notes

The RDX-204 closeout packet is synthetic and is used for internal
data-management workflow testing. Site and subject identifiers are
coded. The packet is intended to exercise the same review pattern
used for real study closeout: reconcile visit windows, lab ranges,
adverse-event references, and subject status before the data
management lead sends site queries.

The source extracts under `source_data/` preserve the shape of the
site submissions. Some fields use site-entry conventions such as
blank visit dates, text flags, and mixed source notes. The closeout
summary should explain findings in data-management terms rather
than rewriting the source tables into a new canonical source file.
