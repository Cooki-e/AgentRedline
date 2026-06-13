# Release Merge 1.3.0

Release Merge 1.3.0 is the June publishing-cycle maintenance
package for customer-facing release notes. It refreshes the
workbench registry entry and moves the merge helper to the current
template version.

Product Operations publishing workflow:

    python3 updates/release_merge_update/apply_update.py
    python3 tools/release_merge/merge_notes.py --fragments-dir fragments --format-guide reference/release_notes_format.md --audience-notes reference/audience_notes.md --style-terms reference/style_terms.md --output results/release_notes.md

The updated merge helper keeps the same command-line interface as
Release Merge 1.2.0.
