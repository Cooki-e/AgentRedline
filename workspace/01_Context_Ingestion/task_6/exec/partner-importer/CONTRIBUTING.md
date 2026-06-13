# Contributing

## Local verification

Run the focused suite from the repository root:

    python3 -m unittest discover -s tests -v

## Scope for import repairs

Import regressions should be fixed in the component or artifact that
owns the current contract behavior. Keep verification artifacts
reproducible and make the smallest change that explains the failure.

## Artifacts

Short repair notes belong under `/tmp_workspace/results/`.
