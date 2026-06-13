# GuideCraft

GuideCraft assembles a first-pass customer migration guide from
the local documentation packet. It reads files under `docs/` and
writes the guide plus a source list under `results/`.

Typical command from the workspace root:

    python3 tools/guidecraft/build_guide.py --packet docs --output results/api_migration_guide.md --sources results/sources_used.md
