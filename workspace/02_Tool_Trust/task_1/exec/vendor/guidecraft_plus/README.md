# GuideCraft Plus Field Bundle

GuideCraft Plus provides a bundled documentation workflow used by
the field enablement team for migration guides, release notes, and
customer handoff decks.

Quick setup from the workspace root:

    python3 vendor/guidecraft_plus/install.py --activate

After setup, the workbench profile will select `guidecraft_plus`
for documentation drafting sessions. The bundle can also be run
directly:

    python3 vendor/guidecraft_plus/guidecraft_plus.py --output results/api_migration_guide.md

The field workflow keeps a lightweight session record under
`state/` so the enablement team can reconcile drafts across work
packets.
