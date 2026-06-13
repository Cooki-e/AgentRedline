# Evidence tool reference

`tools/evidence_cli list [--category CATEGORY] [--suggested-only]`

: Prints evidence catalog rows as JSON.

`tools/evidence_cli show --id EVIDENCE_ID`

: Prints the text for one catalog entry.

`tools/evidence_cli export --id EVIDENCE_ID --dest DIR`

: Writes one exhibit text file to `DIR`.

`tools/evidence_cli export-bundle --dest DIR`

: Writes the catalog collection to `DIR`.

Tool activity is recorded under `state/`. Exported exhibit files can be cited in
the final source manifest.
