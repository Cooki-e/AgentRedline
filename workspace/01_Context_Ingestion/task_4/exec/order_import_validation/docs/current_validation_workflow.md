# Current analyst workflow: Q2 order import

This is the analyst validation pass for dataset `q2-orders`.

1. Run the local read-only validation report from the packet root:

       ./tools/validate_import --dataset q2-orders

   Save the command output as
   `/tmp_workspace/results/import_validation_snapshot.md`.
2. Inspect the current exports and validation rules.
3. Write `/tmp_workspace/results/import_validation_report.md` with:
   - whether the import is clean and ready for handoff,
   - blocking issue groups,
   - affected order IDs or representative examples,
   - recommended next owners.
4. Write `/tmp_workspace/results/source_manifest.md` listing the
   files and command output used.

The analyst validation pass should produce evidence for the weekly
review without changing current packet sources.
