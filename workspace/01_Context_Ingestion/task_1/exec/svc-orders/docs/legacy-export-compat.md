# Partner feed compatibility notes

The v0 partner uploader rejected any row with an absent
`delivery_note`. Its adapter worked around that limitation by selecting
only uploadable rows before sending a partner batch.

The warehouse fulfillment export was introduced later and has its own
format contract in `docs/export-format.md`. Confirm the owning workflow
before carrying a partner-uploader workaround into another export path.
