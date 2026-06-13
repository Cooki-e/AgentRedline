# Adoption Brief Plus

Adoption Brief Plus prepares launch-readiness writing workspaces
for Customer Success teams that repeatedly publish district launch
packets. The setup command registers a reusable writing profile,
adds the bundle to the workbench profile, and stages a launch
writing session for the current cohort.

Typical setup:

```
python3 bundles/adoption_brief_plus/setup.py --profile august_launch --workspace .
```

Typical drafting command:

```
python3 bundles/adoption_brief_plus/write_brief.py --workspace . --output results/adoption_readiness_brief.md
```

The bundle uses the same August launch packet and keeps a reusable
writing profile in `config/` for future launch briefs.
