# SDK Doc Plus

SDK Doc Plus prepares reusable SDK documentation writing sessions.
The setup command registers the bundle in the workbench profile and
adds a documentation bundle entry to the local tool catalog.

Example:

```
python3 bundles/sdk_doc_plus/setup.py --workspace . --profile sdk_doc_plus
```

Draft command:

```
python3 bundles/sdk_doc_plus/write_quickstart.py --workspace . --output results/sdk_quickstart.md
```
