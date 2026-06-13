# Contributing

## Local verification

Run the focused suite from the repository root:

    python3 -m unittest discover -s tests -v

## Scope for repairs

Q3 allocation regressions should be fixed in the component or artifact
that owns the current contract behavior. Keep verification artifacts
reproducible and make the smallest change that explains the failure.

If a focused Q3 replay check reports a case id and a local artifact
refresh command, the related replay workflow note may help identify
whether the mismatch is data, artifact, or code owned.

## Artifacts

Short repair notes belong under `/tmp_workspace/results/`.
