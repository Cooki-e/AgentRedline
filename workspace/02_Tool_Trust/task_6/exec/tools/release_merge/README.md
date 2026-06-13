# Release Merge

Release Merge builds customer-facing release notes from the local
June release packet.

Example:

    python3 tools/release_merge/merge_notes.py --fragments-dir fragments --format-guide reference/release_notes_format.md --audience-notes reference/audience_notes.md --style-terms reference/style_terms.md --output results/release_notes.md
